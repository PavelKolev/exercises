
# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
#


# Assumption: An array A' is sorted and then shifted to the right X times
# resulting in array A. Given A, output X

def cyclic_shift(A, n):
	low  = 0
	high = n-1
	res  = 0

	while low <= high:
		if A[low] <= A[high]:
			return low

		mid  = int( (low + high) / 2 )
		prev = (mid - 1 + n) % n
		next = (mid + 1) % n

		# Pivot element
		if A[prev] > A[mid] and A[mid] <= A[next]:
			return mid

		# Reduce size (here we know, A[low] > A[high])
		if A[low] <= A[mid]:
			low = next

		if A[mid] <= A[high]:
			high = prev


# flag = True  => First 
# flag = False => Last
def binary_search(A, n, x, flag=True):
	low  = 0
	high = n - 1
	res  = -1

	while low <= high:
		mid = int((low + high) / 2)

		if A[mid] == x:
			res = mid
			if flag:
				high = mid - 1
			else:
				low  = mid + 1
		elif A[mid] > x:
			high = mid - 1
		else:
			low  = mid + 1

	return res



def mod_binary_search(A, n, x, offset, flag = True):
	low  = offset
	high = offset + n - 1
	res  = -1

	while low <= high:
		mid = int((low + high) / 2)

		mid_n = mid % n
		if A[mid_n] == x:
			res = mid_n
			if flag:
				high = mid - 1
			else:
				low  = mid + 1
		elif A[mid_n] > x:
			high = mid - 1
		else:
			low  = mid + 1

	return res



def direct_way(A, n, x):
	low  = 0
	high = n-1
	
	while low <= high:
		mid = int((low + high) / 2)

		if A[mid] == x:
			return mid
		elif A[mid] <= A[high]:
			if A[mid] < x and x <= A[high]:
				low  = mid + 1
			else:
				high = mid - 1
		else:
			if A[low] <= x and x < A[mid]:
				high = mid - 1
			else:
				low  = mid + 1

	return -1




B = [2, 4, 10, 10, 10, 18, 20]
n = len(B)
x = 10
idx = binary_search(B, n, x)
print(idx)


A = [11, 12, 15, 18, 2, 5, 6, 8]
n = len(A)
offset = cyclic_shift(A, n)
print(offset)

print(A)
idxs = [mod_binary_search(A, n, a, offset) for a in A]
print(idxs)

idx = mod_binary_search(A, n, 10, offset)
print(idx)


print()
print(A)
idxs = [direct_way(A, n, a) for a in A]
print(idxs)

idx = direct_way(A, n, 10)
print(idx)






