
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
#

import numpy as np


def knapsack(V, W, c, n):
	A = np.zeros( (n, c+1), dtype=np.int32 )
	P = np.zeros( (n, c+1), dtype=np.int32 )

	for j in np.arange(W[0],c+1):
		A[0][j] = V[0]
		P[0][j] = 1

	for i in np.arange(1,n):
		for j in np.arange(W[0],c+1):
			curr_alt = V[i] + A[i-1][j - W[i]] if j >= W[i] else 0
			A[i][j]  = max(A[i-1][j], curr_alt)

			if curr_alt > A[i-1][j]:
				P[i][j] = 1

	row = n-1
	clm = c
	R = []
	while row >= 0:
		if P[row][clm] == 1:
			R.append(row)
			clm -= W[row]
		row -= 1

	return R, A, P


def test():
	V = [6, 10, 12] 
	W = [1, 2, 3] 
	c = 5
	n = len(V)

	print("V:", V)
	print("W:", W)

	sol, A, P = knapsack(V, W, c, n)
	
	print("c:", list(range(c+1)))
	print("A:")
	print(A)
	print("P:")
	print(P)
	print("Solution:")
	print(sol)
	


test()