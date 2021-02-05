


# https://www.geeksforgeeks.org/merging-intervals/
#


I = [[1,3], [4,6], [7,8], [2,5], [6,7]]
I = [[1,5], [2,3], [4,6], [7,8], [8,10], [12,15]]


def merge(A, B):
	L = A.copy()
	R = B.copy()
	Z = []
	
	while L != [] and R != []:
		if L[0][0] <= R[0][0]:
			Z.append(L.pop(0))
		else:
			Z.append(R.pop(0))

	Q = L if L != [] else R
	Z = Z + Q

	return Z


def merge_sort(Q):
	n = len(Q)
	if n <= 1:
		return Q

	mid = n//2
	L = merge_sort(Q[:mid])
	R = merge_sort(Q[mid:])

	N = merge(L, R)
	return N


def solve():
	n = len(I)
	Q = merge_sort(I)

	R = [Q[0]]
	k = 0

	for i in range(1,n):
		if Q[i][0] <= R[k][1]:
			R[k][1] = max( R[k][1], Q[i][1] )
		else:
			R.append(Q[i])
			k += 1

	return R

	
def test():
	print(I)

	R = solve()
	print(R)


test()