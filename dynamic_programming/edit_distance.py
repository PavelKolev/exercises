
# https://www.geeksforgeeks.org/edit-distance-dp-5/
#


# S = source word
# T = target word
def edit_distance(S, n_s, T, n_t):

	# direction matrix
	D = [ [['0'] for  j in range(n_t)] for i in range(n_s) ]
	# minimal edit distance
	A = [ [0 for j in range(n_t)] for i in range(n_s) ]

	# Possible directions
	# R - remove (up)
	# U - update (left-up)
	# I - insert (left)
	# 0 - match  (left-up)
	#
	for j in range(1,n_t):
		D[0][j] = ['I']
		A[0][j] = j

	for i in range(1,n_s):
		D[i][0] = ['R']
		A[i][0] = i

	# Optimal Subproblem - DP
	#
	for i in range(1,n_s):
		for j in range(1,n_t):
			
			if S[i] == T[j]:
				A[i][j] = A[i-1][j-1]
				D[i][j] = ['0']
			
			else:
				#update, #insert, #remove
				L = [ (A[i-1][j-1], 'U'), (A[i][j-1], 'I'), (A[i-1][j], 'R') ]
				m = min([x for x,y in L])
			 
				A[i][j] = 1 + m
				D[i][j] = [y for x,y in L if x == m]

	return A, D



def dfs(D, S, T, i, j, W, R):
	if i == 0 and j == 0:
		R.append(W)
		return

	for d in D[i][j]:
		nw = W.copy()
		
		if d == '0':
			nw.insert(0, (S[i], '0'))
			dfs(D, S, T, i-1, j-1, nw, R)

		elif d == 'I':
			nw.insert(0, (T[j], 'I'))
			dfs(D, S, T, i, j-1, nw, R)

		elif d == 'U':
			nw.insert(0, ([S[i], T[j]], 'U'))
			dfs(D, S, T, i-1, j-1, nw, R)

		else: # d == 'R':
			nw.insert(0, (S[i], 'R'))
			dfs(D, S, T, i-1, j, nw, R)
	


def test():
	S  = '$sun'
	#S  = '$AB'
	n_s = len(S)

	T  = '$satur'
	#T = '$CBAAB'
	n_t = len(T)

	print(' ', list(T))
	print('------------------------------------')
	A, D = edit_distance(S, n_s, T, n_t)
	for i, row in enumerate(A):
		print(S[i], row)
	
	print()
	for i, row in enumerate(D):
		print(S[i], row)

	print()
	W = []
	R = []
	dfs(D, S, T, n_s-1, n_t-1, W, R)
	print(A[n_s-1][n_t-1], R)
	
test()
