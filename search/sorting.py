




import numpy as np

def merge(L,R):
	i, j = 0, 0
	n_L = len(L)
	n_R = len(R)
	S = []

	while i <= n_L-1 and j <= n_R-1:
		if L[i] <= R[j]:
			S.append(L[i])
			i += 1
		else:
			S.append(R[j])
			j += 1

	if i == n_L:
		S.extend(R[j:])
	if j == n_R:
		S.extend(L[i:])

	return S


def merge_sort(S):
	n = len(S)
	if n == 1:
		return S

	mid = int(n/2)

	L = merge_sort(S[:mid])
	R = merge_sort(S[mid:])
	Q = merge(L,R)

	return Q


def quick_sort(S):
	n = len(S)
	if n <= 1:
		return S

	p = np.random.randint(n)
	L = [x for i, x in enumerate(S) if x <= S[p] and i != p]
	R = [x for x in S if x > S[p]]

	Q_L = quick_sort(L)
	Q_L.append(S[p])
	if len(R) > 0:
		Q_R = quick_sort(R)
		Q_L.extend(Q_R)
	
	return Q_L


def test():
	L = [13,21,1,1,4,11,2,7,3,8,6,9,5]
	
	print(L)

	R = merge_sort(L)
	print("Merge Sort:", R)

	R = quick_sort(L)
	print("Quick Sort:", R)


test()


