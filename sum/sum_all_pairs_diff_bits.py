



# https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
#

import math
import time


def to_bits(n, bits):
	s = ''

	while (n // 2) != 0:
		s += str(n % 2)
		n = int( (n - n % 2) / 2 )
	
	s += str(n % 2)
	s = s[::-1]

	t = len(s)
	if t < bits:
		z = '0' * (bits - t)
		s = z + s

	return s


def solve(L):
	n_bits = math.ceil(math.log(max(L), 2))

	LB = []
	for x in L:
		LB.append(to_bits(x, n_bits))

	res = 0
	for i in range(n_bits):
		z, n = 0, 0
		
		for B in LB:
			if B[0] == '0':
				z += 1
			else:
				n += 1
		
		LB = [B[1:] for B in LB]
		res += z * n

	return 2 * res


def test_bits():
	for i in range(9):
		b = to_bits(i)
		print(i, b)


def test():
	start = time.time()
	
	L = list(range(1,100000))

	r = solve(L)
	print(r)

	end = time.time()
	print(end - start)

	

#test_bits()
test()