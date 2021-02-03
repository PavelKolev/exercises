


# https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
#

import numpy as np


# rotate anti clock wise

def swap(M, i, j, l, n):
	T 			  = M[i][j+n-l]
	M[i][j+n-l]   = M[i+n-l][j+n]
	M[i+n-l][j+n] = M[i+n][j+l]
	M[i+n][j+l]   = M[i+l][j]
	M[i+l][j]     = T


def rot_acw(M, i, j, n):
	if i >= n:
		return

	for l in range(n-i):
		swap(M, i, j, l, n-i)

	rot_acw(M, i+1, j+1, n-1)


def load(n):
	M = np.arange(1, n**2 + 1)
	M = np.reshape(M, (n,n))

	M = list(M)
	for i in range(n):
		M[i] = list(M[i])

	return M


def prt(M):
	n = len(M)
	for i in range(n):
		s = ''
		for j in range(n):
			s += '{:2d}'.format(M[i][j])
			s += ' '
		print(s)
	print()


def test():
	n = 5
	M = load(n)

	prt(M)
	rot_acw(M, 0, 0, n-1)
	prt(M)
	
test()