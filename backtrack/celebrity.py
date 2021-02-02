
# https://www.geeksforgeeks.org/the-celebrity-problem/
#

M = [	[0, 0, 1, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 0],
		[0, 0, 1, 0]	]

M = [	[0, 0, 0, 1],
		[0, 0, 0, 1],
		[0, 0, 0, 1],
		[0, 0, 0, 0]	]

# M = [	[0, 0, 0, 0],
# 		[1, 0, 1, 0],
# 		[1, 1, 0, 0],
# 		[1, 0, 0, 1]	]

# M = [	[0, 0, 1, 0],
# 		[0, 0, 1, 0],
# 		[0, 1, 0, 0],
# 		[0, 0, 1, 0]	]



def solve(u,Q,n):
	T = Q.copy()

	for v in T:
		Q.remove(v)
		if M[u][v] == 1:
			return solve(v,Q,n)

	for v in range(n):
		if not {v}.issubset(T):
			if M[u][v] == 1:
				return -1

	return u


def test():
	n = len(M)
	
	Q = set(range(n))
	u = Q.pop()

	idx = solve(u, Q, n)
	print(idx)


test()