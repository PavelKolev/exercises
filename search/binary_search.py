

# Outputs an index such that A[idx] = x
def bin_search(A, n, x):
	low  = 0
	high = n-1
	res  = -1

	while low <= high:
		mid = int( (low + high) / 2 )

		if A[mid] == x:
			res = mid
			return res
		elif x < A[mid]:
			high = mid - 1
		else:
			low  = mid + 1

	return res


# flag == True -> beginning
# flag == False -> beginning
def binary_search(A, n, x, flag = True):
	low  = 0
	high = n-1
	res  = -1

	while low <= high:
		mid = int( (low + high) / 2 )

		if A[mid] == x:
			res = mid
			
			if flag:
				high = mid - 1
			else:
				low  = mid + 1

		elif x < A[mid]:
			high = mid - 1

		else:
			low  = mid + 1

	return res


def count_occurrences(A, n, x):
	start_idx = binary_search(A, n, x)
	end_idx   = binary_search(A, n, x, flag=False)
	return end_idx - start_idx + 1




A = [2, 4, 10, 10, 10, 18, 20]
n = len(A)
x = 10

idx = bin_search(A, n, x)
print(idx)

idx = binary_search(A, n, x)
print(idx)

idx = binary_search(A, n, x, flag=False)
print(idx)

cnt = count_occurrences(A, n, x)
print(cnt)











