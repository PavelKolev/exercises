
# https://www.geeksforgeeks.org/sudoku-backtracking-7/
#
## optimized
#


import numpy as np

G = [   [3, 0, 6,  5, 0, 8,  4, 0, 0], 
		[5, 2, 0,  0, 0, 0,  0, 0, 0], 
		[0, 8, 7,  0, 0, 0,  0, 3, 1],

		[0, 0, 3,  0, 1, 0,  0, 8, 0], 
		[9, 0, 0,  8, 6, 3,  0, 0, 5], 
		[0, 5, 0,  0, 9, 0,  6, 0, 0], 

		[1, 3, 0,  0, 0, 0,  2, 5, 0], 
		[0, 0, 0,  0, 0, 0,  0, 7, 4], 
		[0, 0, 5,  2, 0, 6,  3, 0, 0]	]

# G = [	[3, 1, 6,  5, 7, 8,  4, 9, 2 ],
# 		[5, 2, 0,  1, 3, 4,  0, 6, 8 ],
# 		[4, 8, 7,  6, 2, 9,  5, 3, 1 ],

# 		[2, 6, 3,  0, 1, 5,  0, 8, 7 ],
# 		[9, 7, 4,  8, 6, 0,  1, 2, 5 ],
# 		[0, 5, 1,  7, 9, 2,  6, 4, 3 ],

# 		[1, 3, 8,  0, 4, 7,  2, 0, 6 ],
# 		[0, 9, 0,  3, 5, 1,  8, 7, 4 ],
# 		[7, 4, 5,  0, 8, 6,  3, 1, 0 ]	]


def solve(G):
	#Initialize

	R = [[] for i in range(9)]
	C = [[] for i in range(9)]
	P = [[] for i in range(9)]

	# Rows
	for i in range(9):
		U = [0 for i in range(10)]

		for j in range(9):
			if G[i][j] != 0:
				U[ G[i][j] ] = 1

		R[i] = [j for j in range(1,10) if U[j] == 0]

	# Columns
	for i in range(9):
		U = [0 for i in range(10)]

		for j in range(9):
			if G[j][i] != 0:
				U[ G[j][i] ] = 1

		C[i] = [j for j in range(1,10) if U[j] == 0]

	# 3x3 Patches
	k = 0
	for i in range(3):
		for j in range(3):
			
			L = [G[a][b] for a in range(3*i, 3*i+3) 
						 for b in range(3*j, 3*j+3)]

			U = [0 for i in range(10)]

			for q in range(9):
				if L[q] != 0:
					U[ L[q] ] = 1

			P[k] = [j for j in range(1,10) if U[j] == 0]
			k += 1

	# RUN Backtrack
	S = [[G[i][j] for j in range(9)] for i in range(9)]
	o = backtrack(0, S, R, C, P)

	return S, o


def backtrack(t, S, R, C, P):
	if t == 81:
		return True

	i = t // 9
	j = t % 9

	if S[i][j] != 0:
		return backtrack(t+1, S, R, C, P)

	# Else G[i][j] == 0 -> have to guess it

	p = 3 * (i // 3) + j // 3

	if R[i] == [] or C[j] == [] or P[p] == []:
		#print("-1-------")
		return False

	I = list(set(set(R[i]).intersection(C[j])).intersection(P[p]))
	
	for v in I:
		R[i].remove(v)
		C[j].remove(v)
		P[p].remove(v)

		S[i][j] = v

		#print(i,j,v)

		res = backtrack(t+1, S, R, C, P)
		if res == True:
			return True

		R[i].append(v)
		C[j].append(v)
		P[p].append(v)
		S[i][j] = 0

	#print("-2-------")
	return False



def check(L):
	# contains 1,2,...,9
	# no duplicates
	H = {}
	for i in range(1,10):
		H[i] = 0

	for v in L:
		H[v] += 1

	mm = min(H.values())
	mM = max(H.values())
	
	return mm == 1 and mM == 1


def verify_solution(S):
	R = np.array(S)
	
	for i in range(3):
		for j in range(3):
			
			M = R[3*i : 3*i+3, 3*j : 3*j+3]
			L = np.reshape(M, -1)

			res = check(L)
			if res == False:
				print("Patch: ",i,j)
				return False

	for i in range(9):
		row    = check(R[i])
		column = check(R[:,i])
		
		if row == False or column == False:
			print(i, row, column)
			return False

	return True


def test():
	print()

	n = len(G)
	for i in range(n):
		print(G[i])
	print()

	S, o = solve(G)
	print(o)
	for i in range(9):
		print(S[i])

	if o == True:
		chk = verify_solution(S)
		print()
		print("Checked: ", chk)

	
test()



