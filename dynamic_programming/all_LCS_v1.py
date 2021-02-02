

# https://www.geeksforgeeks.org/print-longest-common-sub-sequences-lexicographical-order/
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
#

import numpy as np

def all_LCS(W1, n1, W2, n2):
	A = [ [0 for j in range(n2)] for i in range(n1) ]

	# 0 - left, 1 - up, 2 - left-up
	P = [ [[-1] for j in range(n2)] for i in range(n1) ]

	for j in range(n2):
		if W1[0] == W2[j]:
			A[0][j] = 1
			P[0][j] = [2]
			for l in range(j+1,n2):
				A[0][l] = 1
				P[0][l] = [0]
			break

	for i in range(n1):
		if W2[0] == W1[i]:
			A[i][0] = 1
			P[i][0] = [2]
			for l in range(i+1,n1):
				A[l][0] = 1
				P[l][0] = [1]

	for i in range(1,n1):
		for j in range(1,n2):
			if W1[i] == W2[j]:
				A[i][j] = 1 + A[i-1][j-1]
				P[i][j] = [2]
			else:
				A[i][j] = max(A[i][j-1], A[i-1][j])
				if A[i][j-1] == A[i-1][j]:
					P[i][j] = [0,1]
				elif A[i][j-1] > A[i-1][j]:
					P[i][j] = [0]
				else:
					P[i][j] = [1]

	return A, P


def dfs(P, i, j, L, w, W1, W2):
	if not (i >= 0 and j >= 0):
		L.append(w)
		return

	for direction in P[i][j]:
		if direction == 2:
			w1 = W1[i] + w
			dfs(P, i-1, j-1, L, w1, W1, W2)

		elif direction == 0:
			dfs(P, i, j-1, L, w, W1, W2)

		elif direction == 1:
			dfs(P, i-1, j, L, w, W1, W2)

		else:
			continue


def test():
	W1 = 'GACT'
	W2 = 'AGCAT'

	#W1 = 'GATC'
	#W2 = 'AGAC'

	W1 = "abcabcaa"
	W2 = "acbacba"

	n1 = len(W1)
	n2 = len(W2)

	A, P = all_LCS(W1, n1, W2, n2)

	print("W1:", W1)
	print("W2:", W2)
	print()

	for i in range(n1):
		print(A[i])

	print()
	for i in range(n1):
		print(P[i])

	print()
	L = []
	dfs(P, n1-1, n2-1, L, '', W1, W2)
	L = list(np.unique(L))
	print(L)


test()
