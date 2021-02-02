


# https://www.geeksforgeeks.org/assembly-line-scheduling-dp-34/
#



def factory_lines(A, T, E, X):
	n = len(A[0])
	S = [[0 for j in range(n)] for i in range(2)]
	P = [-1 for j in range(n+1)]

	S[0][0] = E[0] + A[0][0]
	S[1][0] = E[1] + A[1][0]

	for j in range(1,n):
		for i in range(2):
			same = S[i][j-1]
			diff = S[1-i][j-1] + T[1-i][j]
			S[i][j] = A[i][j] + min( same, diff )
			
	f = min(X[0] + S[0][n-1], X[1] + S[1][n-1])
	
	# Compute Path
	P[n] = 0 if f == X[0] + S[0][n-1] else 1
	
	for j in reversed(range(1,n)):
		i    = P[j+1]
		P[j] = i if S[i][j] == S[i][j-1] + A[i][j] else 1-i

	P[0] = P[1]

	return P, f


def test():
	A = [[4, 5, 3, 2],
	     [2, 10, 1, 4]]

	T = [[0, 7, 4, 5],
	     [0, 9, 2, 8]]

	E = [10, 12]

	X = [18, 7]

	path, cost = factory_lines(A, T, E, X)
	print(path)
	print(cost)


test()

