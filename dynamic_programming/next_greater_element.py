
# https://www.geeksforgeeks.org/next-greater-element/
#


def next_greater(L):
	N = len(L)
	D = [ (-1,-1) for i in range(N)]
	
	D[N-1] = (L[N-1], -1)

	for i in reversed(range(N-1)):
		
		n_M = D[i+1][0]
		M   = max(n_M, L[i])
		idx = -1
		
		if L[i] < L[i+1]:
			idx = i+1

		elif L[i] > n_M:
			idx = -1

		else: #  L[i+1] <= L[i] <= D[i+1][0]
			k = D[i+1][1]
			while k != -1:
				if L[i] >= L[k]:
					k = D[k][1]
				else:
					idx = k
					break
		
		D[i] = (M, idx)

	return D



def test():
	#L = [4, 5, 2, 25]
	#L = [13, 7, 6, 12]
	#L = [4, 3, 2, 1]
	L = [0,0,2,1,3,2,0,5,2,3,1,1]
	#L = [10, 1,2,3,4,5,6,7, 1,2,3,4,5,6, 1,2,3,4,5, 11]
	D = next_greater(L)
	
	print("Rng: ", list(range(len(D))))
	print("List:", L)
	print("nIdx:", [y for x,y in D])
	print("Max :", [x for x,y in D])

	
	k = 0
	H = []
	while k != -1:
		H.append((k,L[k]))
		k = D[k][1]
	
	print("Convex Hull")
	print(H)

test()