


# https://www.geeksforgeeks.org/split-array-two-equal-sum-subarrays/
#


import numpy as np


def subset_sum(L):
	N = len(L)
	S = np.sum(L)
	ub = np.int32( S / 2 )

	if S % 2 == 1:
		return False, ub, None, None
	
	A  = np.zeros( (N, ub + 1), dtype=np.int32 )
	P  = np.zeros( (N, ub + 1), dtype=np.int32 )

	for s in np.arange(1, ub + 1):
		if L[0] <= s:
			A[0][s] = L[0]
			P[0][s] = 1

	for x in np.arange(1, N):
		for s in np.arange(1, ub + 1):
			combined = L[x] + A[x-1][s-L[x]] if s-L[x] >= 0 else 0
			A[x][s]  = max( combined, A[x-1][s] )

			if combined > A[x-1][s]:
				P[x][s] = 1

	R = []
	row = N-1
	clm = ub
	while row >= 0:
		if P[row][clm] == 1:
			R.append(L[row])
			clm -= L[row]
		row -= 1

	return A[N-1][ub] == ub, ub, A, P, R
	

def test():
	L = [5,3,2,10]

	print("Input:", L)

	r, ub, A, P, R = subset_sum(L)
	
	print("Result:", r, ub)
	print("A:")
	print(A)
	print("P:")
	print(P)
	print("Solution:")
	print(R)


test()

