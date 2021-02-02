
# https://www.geeksforgeeks.org/unbounded-knapsack-repetition-items-allowed/
#


c = 8
V = [10, 40, 50, 70]
W = [1, 3, 4, 5]   


def knapsack_unbounded(V,W,c):
	D = [0 for i in range(c+1)]
	n = len(V)

	for j in range(c+1):
		D[j] = ( j // W[0] ) * V[0]

	print(W[0], D)
	for i in range(1,n):
		P = D.copy()

		for j in range(c+1):
			res  = V[i] + max(P[j-W[i]], D[j-W[i]]) if j >= W[i] else 0
			D[j] = max( P[j], res )

		print(W[i], D)

	return D[c]



def test():
	print(" ", list(range(c+1)))
	res = knapsack_unbounded(V,W,c)
	print(res)


test()