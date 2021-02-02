


# https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/
# 


def merge(L, R):
	n_l = len(L)
	n_r = len(R)
	
	l = 0
	r = 0
	m = min(n_l, n_r)
	M = []
	
	while l < n_l and r < n_r:
		if L[l] < R[r]:
			M.append(L[l])
			l += 1
		else:
			M.append(R[r])
			r += 1

	if l == n_l:
		M.extend(R[r:])
	else:
		M.extend(L[l:])

	return M


def merge_sort(A):
	n = len(A)
	if n <= 1:
		return A

	mid = int((n / 2))

	L = merge_sort(A[:mid])
	R = merge_sort(A[mid:])
	M = merge(L, R)

	return M


def pythagorean_triplet(L):
	S  = merge_sort(L)
	n  = len(S)

	R = []
	for k in range(n):
		i = 0
		j = n-1
		t = S[k]**2

		while i < j:
			l = S[i]**2 
			r = S[j]**2

			if l + r == t:
				R.append(((S[i], l),(S[j],r),(S[k],t)))
				break
			elif l + r < t:
				i += 1
			else:
				j -= 1

	return R


def test_sorting():
	A = [4,3,2,5,1,7,6]
	M = merge_sort(A)
	print(M)


def test():
	k = 20
	A = list(range(1,k+1))
	
	R = pythagorean_triplet(A)
	
	for x in R:
		print(x)


test()
