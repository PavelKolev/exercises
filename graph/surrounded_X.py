

# https://www.geeksforgeeks.org/given-matrix-o-x-replace-o-x-surrounded-x/
#


M =  [  ['X', 'X', 'X', 'X', 'X'],
		['X', 'O', 'O', 'O', 'X'],
		['X', 'O', 'X', 'O', 'X'],
		['X', 'O', 'O', 'X', 'X'],
		['X', 'X', 'O', 'X', 'X'],
		['X', 'X', 'X', 'X', 'X'], ]


def adj(i, j, m, n):
	N = [(i,j-1), (i-1,j), (i,j+1), (i+1,j)]
	A = [(i,j) for i,j in N if i >= 0 and i <= m-1\
							and j >= 0 and j <= n-1]

	return A


def bfs(A, R, a, b, m, n):
	if not A[a][b]:
		return 

	S = [(a, b)]
	Q = [(a, b)]	

	corner_reached = False
	while S != []:
		x,y = S.pop(0)
		A[x][y] = 0
		
		for i,j in adj(x, y, m, n):
		
			if M[i][j] == 'O':

				if A[i][j]:
					S.append((i,j))
					Q.append((i,j))

				if i == 0 or i == m-1 or j == 0 or j == n-1:
					corner_reached = True

	if not corner_reached:
		for i,j in Q:
			R[i][j] = 1


def solve():
	m = len(M)
	n = len(M[0])
	R = [[0 for j in range(n)] for i in range(m)]
	A = [[1 for j in range(n)] for i in range(m)]

	for i in range(m):
		print(M[i])

	for i in range(1,m-1):
		for j in range(1,n-1):
			if M[i][j] == 'O' and A[i][j]:
				bfs(A, R, i, j, m, n)

	for i in range(m):
		for j in range(n):
			if R[i][j] == 1:
				M[i][j] = '@'

	print()
	for i in range(m):
		print(M[i])



solve()