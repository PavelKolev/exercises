
# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
#


class Node():
	
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


def show_in_order(node, L):
	if node is None:
		return

	show_in_order(node.left, L)
	L.append(node.value)
	show_in_order(node.right, L)


def find_lca(node, v1, v2):
	
	if v1 < node.value and v2 < node.value:
		return find_lca(node.left, v1, v2)

	elif node.value < v1 and node.value < v2:
		return find_lca(node.right, v1, v2)

	else:
		return node
	
	

def test():
	root = Node(3, Node(2, Node(1)),
				   Node(7, Node(5, Node(4), Node(6)), 
						   Node(8, None, 
								   Node(10, Node(9), Node(11)))))
	
	node = find_lca(root, 6, 9)
	print(node.value)

test()