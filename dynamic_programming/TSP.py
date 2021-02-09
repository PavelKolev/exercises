
# https://www.geeksforgeeks.org/travelling-salesman-problem-set-1/
#


#	   1   2   3   4	
A = [[ 0, 10, 15, 20],
	 [10,  0, 35, 25],
	 [15, 35,  0, 30],
	 [20, 25, 30,  0]]


#   choose(n, k, 0, 2, S_i, L)
def choose(n, k, i, l, S_i, L):
	if i == k:
		S = S_i.copy()
		L.append(S)
		return

	for e in range(l, n+2-k+i):
		S_i.add(e)
		choose(n, k, i+1, e+1, S_i, L)
		S_i.remove(e)


def solve(A, n):
	# Initialize the Dictionary (DP Table)
	D = {}

	# Initialize Base case, i.e. edges
	S_I = []
	choose(n, 1, 0, 2, set(), S_I)

	for i in range(2,n+1):
		D[str(i)] = {}
		for j in range(2, n+1):
			D[str(i)][j] = A[1][j] if i == j else float('inf')

	# Main Part
	for v in range(2, n+1):
		S_I = []
		choose(n, v, 0, 2, set(), S_I)

		for S in S_I:
			S_w    = ''.join([str(e) for e in sorted(S)])
			D[S_w] = {}

			for j in range(2, n+1):
				if not (j in S):
					D[S_w][j] = float('inf')

				else: # j in S
					S_j	= S.copy()
					S_j.remove(j)

					S_j_w = ''.join([str(e) for e in sorted(S_j)])

					sols  = [D[S_j_w][i]  + A[i][j] for i in S_j]
					D[S_w][j] = min( sols )

					#print('[', S_w, j, ']=', sols, D[S_w][j])
	return D


def solution(A, D, n):
	# Compute Optimal Value
	S    = set(range(2, n+1))
	S_w  = ''.join([str(e) for e in sorted(S)])
	OPT  = min( [D[S_w][j] + A[j][1] for j in range(2, n+1)] )
	
	# Compute Optimal Solution (the TSP tour)
	V    = [1]
	last = 1
	while S:
		S_w = ''.join([str(e) for e in sorted(S)])
		opt = min( [D[S_w][j] + A[j][last] for j in S] )
		L   = [j for j in S if opt == D[S_w][j] + A[j][last]]
		
		V.insert(0, L[0])
		S.remove(L[0])
		last = L[0]
	
	V.insert(0, 1)
	return V, OPT


def test_choose():
	n = 5

	for i in range(n):
		L = []
		S = set()
		choose(5, i, 0, 2, S, L)

		for Z in L:
			S_str = ''.join([str(e) for e in sorted(Z)])
			print(S_str)

		print()


def run():
	n = len(A)

	# Extend A by 1 dimension (row-column-wise)
	A.insert(0, [0 for i in range(n+1)])
	for i in range(n+1):
		A[i].insert(0, 0)

	# Show Adj matrix A
	for i in range(n+1):
		print(A[i])
	print()

	# Solve TSP problem and show an optimal solution
	D 	   = solve(A, n)
	V, opt = solution(A, D, n)

	print(V, opt)


#test_choose()
run()































