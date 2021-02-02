
# Find if a string is interleaved of two other strings | DP-33
# https://www.geeksforgeeks.org/find-if-a-string-is-interleaved-of-two-other-strings-dp-33/
#


# Gready (linear time) algo does not work since
#
# CCA, CAC, CACCAC
# 1. CCA -> ACC != CAC
# 2. CAC -> CAC != CCA
#


import numpy as np

A = '$CAC'
B = '$CCA'
C = '$CACCAC'

#A = '$XAZ'
#B = '$ABC'
#C = '$XAABZC'


def dp(A, m, B, n, C):
	D = [[[] for j in range(n)] for i in range(m)]
	
	# Initialize
	for i in range(1,m):
		if A[1:i+1] == C[1:i+1]:
			D[i][0] = [A[1:i+1]]
		else:
			D[i][0] = D[i-1][0]

	for j in range(1,n):
		if B[1:j+1] == C[1:j+1]:
			D[0][j] = [B[1:j+1]]
		else:
			D[0][j] = D[0][j-1]

	# Main Part

	for i in range(1,m):
		for j in range(1,n):
			w_ij  = C[1:i+j+1]
			ext_A = [x + A[i] for x in D[i-1][j] if x + A[i] == w_ij]
			ext_B = [y + B[j] for y in D[i][j-1] if y + B[j] == w_ij]

			# All feasible words
			L = ext_A + ext_B + D[i-1][j] + D[i][j-1]
			R = [(l, len(l)) for l in L]
			m = max([n_l for l, n_l in R])

			# Select the unique words of maximal length
			Q = [l for l, n_l in R if n_l == m]
			U = list(np.unique(Q))
		
			D[i][j] = U

	return D


def run():
	m = len(A)
	n = len(B)

	D = dp(A, m, B, n, C)

	print("  ",B)
	for i in range(m):
		print(A[i], D[i])
	print("  ",C)

	res = True if D[m-1][n-1][0] == C[1:] else False
	print(res)


run()




