
# https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/
# Egg Dropping Puzzle | DP-11
#

import math


def solve(n,k):
	F = [[0 for j in range(k+1)] for i in range(n+1)]

	# Init
	for j in range(1,k+1):
		F[1][j] = 1
		F[2][j] = 2
		F[3][j] = 2
		F[4][j] = 3
		
	for i in range(1,n+1):
		F[i][1] = i

	# Main
	for i in range(5,n+1):
		for j in range(2,k+1):

			# Check the first half, the other half is same
			L = range(1, (i//2 + 1) + 1)
			R = [max(F[l-1][j-1], F[i-l][j]) for l in L]
			
			F[i][j] = 1 + min( R )

	return F


def test():
	n = 100
	k = 5
	F = solve(n, k)
	
	for i in range(1,n+1):
		print(F[i])
		
test()





