
# https://www.geeksforgeeks.org/print-longest-common-sub-sequences-lexicographical-order/
# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
#


def all_LCS(W1, n1, W2, n2):
	A = [ [ [] for j in range(n2) ] for i in range(n1) ]

	# INITIALIZE first row and column
	# Row
	for j in range(n2):
		if W1[0] == W2[j]:
			for l in range(j, n2):
				A[0][l].append([W1[0]])
			break

	# Column
	for i in range(n1):
		if W1[i] == W2[0]:
			for l in range(i, n1):
				A[l][0].append([W2[0]])
			break
	
	for i in range(n1):
		print(A[i])
	# Apply Dynamic Programming
	#
	for i in range(1,n1):		
		for j in range(1,n2):
			print("i,j:", i, j)

			if W1[i] == W2[j]:
				print("A[i-1][j-1] = ", A[i-1][j-1])
				if len(A[i-1][j-1]) == 0:
					A[i][j].append( [W1[i]] )
				else:
					for x in A[i-1][j-1]:
						r = x.copy()
						r.append(W1[i])
						A[i][j].append(r)

			else:
				R = []
				
				if A[i-1][j] != [] and A[i][j-1] != []:
					print("Being: A[i-1][j]", A[i-1][j])
					print("Being: A[i][j-1]", A[i][j-1])

					s1 = len(A[i-1][j][0])
					s2 = len(A[i][j-1][0])
					
					if s1 == s2:
						R.extend(A[i-1][j])
						R.extend(A[i][j-1])
						print("R1:", R)
						A[i][j] = R

					elif s1 > s2:
						R.extend(A[i-1][j])
						A[i][j] = R
						print("R2:", R)
					else:
						R.extend(A[i][j-1])
						A[i][j] = R
						print("R3:", R)

				elif A[i-1][j] != []:
					R.extend(A[i-1][j])
					A[i][j] = R
					print("R4:", R)

				else:
					R.extend(A[i][j-1])
					A[i][j] = R
					print("R5:", R)

			print("A[i][j]:", A[i][j])

	return A




W1 = ['G','A','C']
W2 = ['A','G','C','A','T']

#W1 = ['G','A','T','C']
#W2 = ['A','G','A','C']

n1 = len(W1)
n2 = len(W2)

L = all_LCS(W1, n1, W2, n2)
for i in range(n1):
	print(L[i])

