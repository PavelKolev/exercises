


#https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/
#
# Without any assumptions:
#
# Build a balanced search tree (for instance AVL)
# Augument the AVL to include the following data
#
# minimum over the current node and all nodes in its left and right subtree
# w.r.t. the index in list L corresponding the value of each node.
#
# Then upon the arrival of a new node, find the largest node in AVL that
# has smaller value than the current, and return the minimum index of this subtree
# which is stored in this very node
#
# Insert the node and update the minimum index along the path to the root. 
#
#
# Assuming Input with Unique Elements
# Observation: The problem reduces to computing the rank in non-increasing order 
# of the elements in the input list L. Then a Greedy Strategy suffices, 
# using Hashing and Maintaning List of pairs (minimum and maximum observed rank).
#

def merge(L, R):
	Q = []
	
	while L != [] and R != []:
		if L[0] <= R[0]:
			Q.append(L[0])
			L.pop(0)
		else:
			Q.append(R[0])
			R.pop(0)

	Q += L if L != [] else R
	return Q


def merge_sort(Q):
	n = len(Q)
	if n <= 1:
		return Q

	mid = n // 2
	L   = merge_sort(Q[:mid])
	R   = merge_sort(Q[mid:])
	Z   = merge(L, R)

	return Z


# Assuming there is an element in B[:][0] with value smaller than r_j
# return the smallest index i in [0:h] such that B[i][0] < r_j
#
def bs_max_smallest(B, l, h, r_j):
	
	while l < h:
		mid = (h+l) // 2

		if B[mid][0] < r_j:
			h = mid
		else:
			l = mid+1

	return h


def solve(L):
	n = len(L)
	R = {} # mapping L[i] -> rank of L[i] in non-decreasing sorted order
	B = [] #[(lower seen Rank, upper seen Rank) for _ in range(n)]

	sol = (-1,-1)
	val = 0

	S = merge_sort(L)
	for i in range(n):
		R[S[i]] = i+1

	B.append( [ R[L[0]], R[L[0]] ] )
	for j in range(1,n):
		min_Rj = min( B[j-1][0], R[L[j]] )
		max_Rj = max( B[j-1][1], R[L[j]] )
		
		B.append([min_Rj, max_Rj])

		# more than the previous maximum
		if B[j-1][1] < R[L[j]]:
			val = j
			sol = (0,j)

		# less than the previous minimum
		elif R[L[j]] <= B[j-1][0]:
			continue

		# B[j-1][0] < R[L[j]] <= B[j-1][1]
		else: 
			i = bs_max_smallest(B, 0, j-1, R[L[j]])
			if j-i > val:
				val = j-i
				sol = (i,j)

	return sol


def test():
	L = [ [34, 8, 10, 3, 2, 80, 30, 33, 1],
	 	  [9, 2, 3, 4, 5, 6, 7, 8, 18, 0],
	 	  [1, 2, 3, 4, 5, 6],
	 	  [6, 5, 4, 3, 2, 1] ]

	n = len(L)
	for t in range(n):
		i,j = solve(L[t])
		
		print(L[t])
		if (i,j) != (-1,-1):
			print(j-i, [i, L[t][i]], [j, L[t][j]])
		else:
			print(j-i, [i, -1], [j, -1])
		print()


test()




