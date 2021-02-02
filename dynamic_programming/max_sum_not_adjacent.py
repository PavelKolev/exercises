


# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
#


def max_sum_not_adj(A):
	n = len(A)
	R = [0  for i in range(n)]
	U = [0 for i in range(n)]
	
	R[0] = A[0]
	R[1] = max(A[0], A[1])
	U[0] = 1
	U[1] = 1 if A[1] >= A[0] else 0

	for i in range(2,n):
		p2   = A[i] + R[i-2]
		p1   = R[i-1]
		R[i] = max(p2, p1)
		U[i] = 1 if p2 > p1 else 0

	S = []
	k = n-1

	while k >= 0:
		if U[k] == 1:
			S.insert(0, (k, A[k]))
			k -= 2
		else:
			k -= 1

	return R, S


def test():
	A = [21,11,90,100,10,15]
	#A = [9, 11, 10, 7, 21, 22]
	#A = [5, 5, 10, 100, 10, 5]

	R, S = max_sum_not_adj(A)
	
	print(A)
	print()
	print(S)
	print(R)
	

test()

