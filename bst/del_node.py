
# https://www.geeksforgeeks.org/deletion-binary-tree/
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
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




# No Duplicate values in the BST
# Root in not to be removed

# RECURSIVE

# assume node != None
def find_min(node):
	if node.left == None:
		return node.value
	else:
		return find_min(node.left)


def delete_node(root, value):
	if root == None:
		return None

	if value < root.value:
		root.left  = delete_node(root.left, value)
		return root

	elif root.value < value:
		root.right = delete_node(root.right, value)
		return root

	else: # root.value = value
	
		# case 1. two children
		if root.left != None and root.right != None:
			min_value  = find_min(root.right)
			root.value = min_value
			root.right = delete_node(root.right, min_value)
			return root

		# case 2. a leaf node
		elif root.left == None and root.right == None:
			return None

		# case 3. one child
		else:
			# only left child
			if root.left != None:
				return root.left

			# only right child
			else:
				return root.right




# ITERATIVE

# find a BST node
def find(par, node, value, dir=None):
	if node == None:
		return (None, None, dir)

	if node.value == value:
		return (par, node, dir)

	if value < node.value:
		return find(node, node.left, value, 0)
	else:
		return find(node, node.right, value, 1)


def find_smallest(par, node):
	if node.left == None:
		return (par, node)
	else:
		return find_smallest(node, node.left)


def set(par, dir, node):
	if dir == 0:
		par.left  = node
	else:
		par.right = node


# delete a BST node
def del_node(root, value):
	par, node, dir = find(None, root, value)

	if node.left == None and node.right == None:
		set(par, dir, None)

	elif node.right != None:
		s_par, s_node = find_smallest(node, node.right)

		if node.right.left != None:
			s_par.left = None
		else:
			s_par.right = None

		# update current node
		node.value = s_node.value

	else: #node.left != None:
		if par != None:
			set(par, dir, node.left)
		else:
			left_node  = root.left
			root.value = left_node.value
			root.right = left_node.right
			root.left  = left_node.left


def test():
	(par, node) = find(None, root, 2)
	pv = par.value if par != None else None
	nv = node.value if node != None else None
	print(pv, nv)




def test_delete():
	root = Node(8, Node(4, Node(2), Node(5, Node(4.1), Node(6))),
				   Node(10, Node(9, Node(8.1), Node(9.1)), Node(11)) )

	ST = []
	in_order(root, ST)
	print(ST)

	delete_node(root, 4)

	ST = []
	in_order(root, ST)
	print(ST)


test_delete()