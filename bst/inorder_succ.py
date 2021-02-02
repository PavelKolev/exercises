
# https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/
#



class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right
		
# Simplest
def in_order(node, L):
	if node == None:
		return

	in_order(node.left, L)
	L.append(node.value)
	in_order(node.right, L)


def find_min(node):
	if node.left == None:
		return node.value
	else:
		return find_min(node.left)


# anc = the closest ancestor of the target node such that
#       target node is in Left-Tree[Ancestor].
def in_order_succ(root, value, anc=None):
	if root == None:
		return -1

	if value < root.value:
		return in_order_succ(root.left, value, root)
	
	elif root.value < value:
		return in_order_succ(root.right, value, anc)

	else: # root.value == value
		if root.right != None:
			return find_min(root.right)
		else:
			if anc != None:
				return anc.value
			else:
				return -1



def test_delete():
	root = Node(8, Node(4, Node(2), Node(5, Node(4.1), Node(6))),
				   Node(10, Node(9, Node(8.1), Node(9.1)), Node(11)) )

	ST = []
	in_order(root, ST)
	print(ST)

	for x in ST:
		print(x, in_order_succ(root, x))


test_delete()