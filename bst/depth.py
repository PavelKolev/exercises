


class Node():
	
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


def depth(node):
	if node == None:
		return -1, -1

	l_m, l_M = depth(node.left)
	r_m, r_M = depth(node.right)

	return 1 + min(l_m, r_M), 1 + max(l_M, r_M)



def test():
	root = Node(-1, Node(12),
					Node(10, Node(2, Node(20), Node(2)), 
							 Node(10, None, 
								 	  Node(-25, Node(3), Node(4)))))


	m, M = depth(root)
	print("Min: ", m, "Max: ", M)


test()