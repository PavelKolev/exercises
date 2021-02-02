



# https://www.geeksforgeeks.org/the-stock-span-problem/
#


def stock_span(L):
	n = len(L)
	D = [1 for i in range(n)]
	S = [0]

	for i in range(1,n):
		if L[i] < L[i-1]:
			S.insert(0, i)
			continue

		#L[i] >= L[i-1]:
		while S:
			if L[i] >= L[S[0]]:
				j = S.pop(0)
				D[i] += D[j]
			else:
				break
		S.insert(0, i)
	
	return D, S


def test():
	L = [[100, 80, 60, 70, 60, 75, 85],
	 	 [1, 1, 1, 2, 1, 4, 6]]

	L = [[100, 120, 130, 90, 70, 80, 92, 129],
		 [1, 2, 3, 1, 1, 2, 4, 5]]

	D, S = stock_span(L[0])
	print(S)
	print(D)
	print(L[1])


test()

