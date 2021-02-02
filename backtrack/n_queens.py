
# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
#


def n_queens(A, i, n, C, S):
	if i == n:
		S.append(list(reversed(C)))
		return

	for j in A[i]:
		
		X = [s.copy() for s in A]
		C.insert(0, (i,j))

		for l in range(i+1,n):
			
			if j in X[l]:
				X[l].remove(j)

			if j+l-i <= n-1:
				if j+l-i in X[l]:
					X[l].remove(j+l-i)

			if j-l+i >= 0:
				if j-l+i in X[l]:
					X[l].remove(j-l+i)

		n_queens(X, i+1, n, C, S)
		C.pop(0)


def test():
	n = 4
	A = [set([j for j in range(n)]) for i in range(n)]
	C = []
	S = []

	n_queens(A, 0, n, C, S)
	for s in S:
		M = [[0 for j in range(n)] for i in range(n)]
		
		for i,j in s:
			M[i][j] = 1
		
		for i in range(n):
			print(M[i])
		print()
		

test()


