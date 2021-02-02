


# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
#

def spiral(A, m, n):
	T, L = 0, 0
	B, R  = m-1, n-1
	dir = 0

	res = []
	while T <= B and L <= R:
		if dir == 0:
			for j in range(L, R+1):
				res.append(A[T][j])
			T += 1
		
		elif dir == 1:
			for i in range(T, B+1):
				res.append(A[i][R])
			R -= 1

		elif dir == 2:
			for j in reversed(range(L,R+1)):
				res.append(A[B][j])
			B -= 1

		elif dir == 3:
			for i in reversed(range(T,B+1)):
				res.append(A[i][L])
			L += 1

		dir = (dir + 1) % 4

	return res


A = [ [1,2,3,4],
	  [12,13,14,5],
	  [11,16,15,6],
	  [10,9,8,7] ]

res = spiral(A, 4, 4)
print(res)







