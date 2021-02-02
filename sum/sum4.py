
# https://www.geeksforgeeks.org/find-four-elements-that-sum-to-a-given-value-set-2/
#

from random import randint


def partition(Q, mid):
	L, R = [], []
	
	for i in range(len(Q)):
		if i == mid:
			continue

		if Q[i][0] <= Q[mid][0]:
			L.append(Q[i])
		else:
			R.append(Q[i])

	return L, R


def quick_sort(Q):
	n = len(Q)
	if n <= 1:
		return Q

	mid    = randint(0,n-1)
	LQ, RQ = partition(Q, mid)

	L = quick_sort(LQ) if LQ != [] else []
	R = quick_sort(RQ) if RQ != [] else []

	return L + [ Q[mid] ] + R


def solve(L, x):
	n = len(L)
	Q = []

	for i in range(n):
		for j in range(n):
			if i < j:
				Q.append((L[i] + L[j], [i, j]))
	
	Z = quick_sort(Q)
	
	m = Z[0][0]  + Z[1][0]
	M = Z[-2][0] + Z[-1][0]
	
	if x < m or M < x:
		return False, [], []

	l = 0
	r = len(Z) - 1

	while l < r:
		s = Z[l][0] + Z[r][0]
		if s < x:
			l += 1
		elif x < s:
			r -= 1
		else: # s == x
			I = set(Z[l][1] + Z[r][1])
			if len(I) == 4:
				return True, Z[l], Z[r]
			else:
				return check(Z, l, r, x)


def check(Z, l, r, x):
	# move left to right
	a = l+1
	b = r
	left = False

	while a < b:
		s = Z[a][0] + Z[b][0]
		if s > x:
			break
		else: # s == x
			I = set(Z[a][1] + Z[b][1])
			if len(I) == 4:
				return True, Z[a], Z[b]
			a += 1

	# move right to left
	a = l
	b = r - 1
	right = False

	while a < b:
		s = Z[a][0] + Z[b][0]
		if s < x:
			break
		else: # s == x
			I = set(Z[a][1] + Z[b][1])
			if len(I) == 4:
				return True, Z[a], Z[b]
			b -= 1

	return False, [], []



def test_QS():
	Q = [[x] for x in [11,31,22,44,4,1,9,11,20,30]]
	R = quick_sort(Q)
	print(R)


def test():
	Q = [1,4,9,11,20,30]
	x = 25
	
	T, L, R = solve(Q, x)
	print(T, L, R)

#test_QS()
test()