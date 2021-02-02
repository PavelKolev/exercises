

# https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
#

class Node():
	
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


def max_path_sum(node):
	if  node == None:
		return 0, 0

	l_p, l_t = max_path_sum(node.left)
	r_p, r_t = max_path_sum(node.right)

	n_p = node.value + max(0, max(l_p, r_p))
	n_t = l_p + node.value + r_p

	return n_p, max(l_t, r_t, n_t)


def test():
	root = Node(-1, Node(12),
					Node(10, Node(2, Node(20), Node(2)), 
							 Node(10, None, 
								 	  Node(-25, Node(3), Node(4)))))


	res = max_path_sum(root)
	print(res)


test()