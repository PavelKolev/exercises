
# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
#

def max_sum_sub_array(L):
	#start i, end j, current l, d max sum
	i, j, d = 0, 0, 0

	d = L[0]
	s = L[0]
	
	iter_L = iter(L)
	next(iter_L)

	k = 1
	for elem in iter_L:
		s_new = s + elem
		
		if s_new >= max(d, elem):
			s = s_new
			d = s_new
			j = k

		if d >= max(s_new, elem):
			s = s_new

		if elem >= max(d,elem):
			s = elem
			d = elem
			i = k

		k += 1

	return L[i:j+1], d 


def test():
	#L = [-3,-1,-2,1,-3,2,-5,7,6,-1,-4,11,-2,3,-23]
	L = [-6,8,3,-1,5,-7,1,2]

	print(L)
	sub_L, s = max_sum_sub_array(L)
	print(sub_L, s)


test()
