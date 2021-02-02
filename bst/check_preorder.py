
# https://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/
#



# Preorder
# Root, Left, Right

def preorder(L):
	m = min(L)
	M = max(L)
	n = len(L)

	Q = []
	Q.insert(0, [L[0], m, M, False, False])

	k = 1
	while k < n and Q:
		print(L[k], Q[0])
		p_v, p_m, p_M, p_l, p_r = Q[0]

		# Left node
		if (not p_l) and p_m <= L[k] and L[k] <= p_v:
			# left is used now
			Q[0][3] = True
			Q.insert(0, [L[k], p_m, p_v, False, False])
			k += 1

		# right node
		elif (not p_r) and p_v <= L[k] and L[k] <= p_M:
			# right is used
			Q[0][4] = True
			Q.insert(0, [L[k], p_v, p_M, False, False])
			k += 1

		# not (p_m <= L[k] and L[k] <= p_M)
		else:
			# Remove parent, as it cannot be used
			# to extend the pre-order
			Q.pop(0)

	return k == n


def test():

	#L = [2, 4, 3]
	#L = [2, 4, 1]
	#L = [5, 3, 4, 8, 10]
	#L = [8, 4,2,1,3,6,5,7, 12,10,9,11,14,13,15]
	L = [8, 12,10,9,11,14,13,15]

	res = preorder(L)
	print(res)



test()
