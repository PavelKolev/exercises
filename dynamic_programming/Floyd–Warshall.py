
# https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
#

def floyd_warshall(A, z):
	n = len(A)

	# D is a copy of A
	S1 = [ [A[i][j] for j in range(n)] for i in range(n) ]
	S2 = [ [A[i][j] for j in range(n)] for i in range(n) ]

	N = [ [None if A[i][j] == z else j for j in range(n)] for i in range(n)]
	
	for k in range(n):
		for i in range(n):
			for j in range(n):
				n_k = S1[i][j]
				y_k = S1[i][k] + S1[k][j]

				#S2[i][j] = min( n_k, y_k )
				if y_k < n_k:
					S2[i][j] = y_k
					N[i][j]  = N[i][k]

					#if i == j:
					#	print(i, j, y_k, n_k)

		for i in range(n):
			for j in range(n):
				S1[i][j] = S2[i][j]

		#print(k)
		#p_mtx(N)
	#print()

	return S1, N


def p_mtx(A):
	n = len(A)
	R = range(n)
	
	print(' ', list(R))
	print('--------------------')
	for i in R:
		print(i, A[i])
	print()


def test():
	z = float('inf')

	      #0, 1, 2, 3, 4, 5
	A = [ [z, 2, 1, 5, z, z], #0
		  [2, z, 2, 3, z, z], #1
		  [1, 2, z, 3, 1, z], #2
		  [5, 3, 3, z, 1, 5], #3
		  [z, z, 1, 1, z, 1], #4
		  [z, z, z, 5, 1, z]] #5

	#       #0, 1, 2, 3, 4
	# A = [ [z, 1, z, z, z], #0
	# 	  [1, z, z, z, 1], #1
	# 	  [z, z, z, 1, z], #2
	# 	  [z, z, 1, z, 1], #3
	# 	  [z, 1, z, 1, z]] #4
		  

	D, N = floyd_warshall(A, z)

	p_mtx(A)
	p_mtx(D)
	p_mtx(N)
	
	


test()
