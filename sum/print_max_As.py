


# https://www.geeksforgeeks.org/how-to-print-maximum-number-of-a-using-given-four-keys/
#

def solve(n):
	B = [0 for x in range(n+1)]
	T = [0 for x in range(n+1)]

	T[1:7] = list(range(1,7))

	for i in range(7,n+1):
		# There are 3 options:
		# print new A

		# select, copy to buffer and paste
		if 2 * T[i-3] > T[i-1] + max( B[i-1], 1 ):
			B[i-1] = T[i-3]
			B[i]   = T[i-3]
			T[i]   = 2 * B[i]

		else: # paste from buffer or print A
			B[i] = B[i-1]
			T[i] = T[i-1] + max( B[i-1], 1 )

	return B, T


def test():
	n = 20

	for i in range(6, n+1):
		B, T = solve(i)
		print(B)
		print(T)
		print()


test()
