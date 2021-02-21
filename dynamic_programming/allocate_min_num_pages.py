

# https://www.geeksforgeeks.org/allocate-minimum-number-pages/
#



def slow_solve(L, m):
	n = len(L)
	T = [[0 for j in range(n)] for i in range(m)]

	# Initialize
	T[0][n-1] = L[n-1]
	for j in reversed(range(n-1)):
		T[0][j] = T[0][j+1] + L[j]

	for i in range(1,m):
		T[i][n-1-i] = L[n-1]

	# Main
	for i in range(1,m):
		# print('\n', T[i-1],'\n')
		for j in reversed(range(n-1-i)):
			sols = [max( T[0][j] - T[0][l+1], T[i-1][l+1] ) for l in range(j,n-i)]
			# print(i,j,sols)
			T[i][j] = min(sols)

	return T


def fast_solve(L, m):
	n = len(L)
	T = [[0 for j in range(n)] for i in range(m)]

	# Initialize
	T[0][n-1] = L[n-1]
	for j in reversed(range(n-1)):
		T[0][j] = T[0][j+1] + L[j]

	for i in range(1,m):
		T[i][n-1-i] = L[n-1]

	# Main
	for i in range(1,m):
		l = n-i-1
		for j in reversed(range(n-1-i)):
			while True:
				curr = max( T[0][j] - T[0][l+1], T[i-1][l+1] )
				prev = max( T[0][j] - T[0][l]  , T[i-1][l] )

				if prev > curr:
					break
				else:					
					l -= 1
			
			T[i][j] = curr

	return T


def test():
	L = [1, 5, 11, 22, 34, 39, 44, 57, 61, 71]
	m = 6

	T = slow_solve(L, m)
	for i in range(m):
		print(T[i])

	print()
	F = fast_solve(L, m)
	for i in range(m):
		print(F[i])

	print()
	n   = len(L)
	Err = [sum( [abs(T[i][j]-F[i][j]) for j in range(n)] ) for i in range(m)]
	err = sum(Err)
	print(err)


test()


