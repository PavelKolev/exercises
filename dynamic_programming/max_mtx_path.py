

# https://www.geeksforgeeks.org/maximum-path-sum-matrix/


def get_Neighbours(i, j, m, n):
    # Left, Up, Right, Down
	L = [(i,j-1), (i-1,j), (i,j+1), ((i+1,j))]
	R = [(x,y) for x,y in L if x >= 0 and x <= m-1 and y >= 0 and y <= n-1]
	return R


def dfs(A, P, D, i, j, m, n):
	if D[i][j] >= 0:
		return

	N   = get_Neighbours(i, j, m, n)
	d_N = [(a,b) for a,b in N if A[i][j] == 1 + A[a][b]]

	if d_N == []:
		D[i][j] = 0
		return

	# (i,j) has a neibour (a,b) such that A[i][j] == 1 + A[a][b]
	a, b    = d_N[0]
	P[i][j] = (a,b)

	dfs(A, P, D, a, b, m, n)
	D[i][j] = 1 + D[a][b]


def max_path(A):
	m = len(A)
	n = len(A[0])

	# -1 no predecessor, 0 left, 1 up, 2 right, 3 down
	P = [ [(-1,-1) for j in range(n)] for i in range(m) ]
	D = [ [-1  for j in range(n)] for i in range(m) ]

	for i in range(m):
		for j in range(n):
			dfs(A, P, D, i, j, m, n)

	return P, D



def path(A, P):
	m = len(A)
	n = len(A[0])
	M = max(max(A))

	L = [(i,j) for j in range(n) for i in range(m) if A[i][j] == M]
	i, j = L[0]

	R = []
	while P[i][j] != (-1, -1):
		R.insert(0, [(i,j), A[i][j]])
		i, j = P[i][j]

	return R



def print_Mtx(A):
	m = len(A)
	for i in range(m):
		print(A[i])
	print()


#A = [ [1,2,9],
#	  [5,3,8],
#	  [4,6,7]]


A = [ [1, 2, 9, 10],
	  [5, 3, 8, 11],
	  [4, 6, 7, 12],
	  [16,15,14,13]]


P, D = max_path(A)
print_Mtx(A)
print_Mtx(P)
print_Mtx(D)

R = path(A, P)
print_Mtx(R)


