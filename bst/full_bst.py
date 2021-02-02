


class Node():
	
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


def full_bst(node):
	if node  == None:
		return True

	if node.left == None and node.right == None:
		return True

	if node.left != None and node.right != None:
		return full_bst(node.left) and full_bst(node.right)

	return False


def test():
	root = Node(-1, Node(12),
					Node(10, Node(2, Node(20), Node(2)), 
							 Node(10, None, 
								 	  Node(-25, Node(3), Node(4)))))

	print(full_bst(root))
	

test()