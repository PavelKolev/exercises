

# Check if a Binary Tree contains duplicate subtrees of size 2 or more
# https://www.geeksforgeeks.org/check-binary-tree-contains-duplicate-subtrees-size-2/



class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


class Node_Ext(Node):

	def __init__(self, node):
		self.value = node.value
		self.left  = node.left
		self.right = node.right
		
		self.depth = 0
		self.o_i   = ''
		self.o_p   = ''
		self.D     = {}


root = Node('A', Node('B', Node('D'), Node('E')),
				 Node('C', Node('B', Node('D'), Node('E')),
				 		   Node('B', Node('D'), Node('E'))))


def in_order(node, L):
	if node == None:
		return

	in_order(node.left, L)
	L.append(node.value)
	in_order(node.right, L)


def pre_order(node, L):
	if node == None:
		return

	L.append(node.value)
	pre_order(node.left, L)
	pre_order(node.right, L)


def view(node):
	if node == None:
		return

	print([node.value, node.d, node.o_i, node.o_p])
	print(node.D)
	print()

	view(node.left)
	view(node.right)



# Extend Tree
#
def extend_tree(node, src):
	if src == None:
		return

	node.left  = Node_Ext(src.left)  if src.left  != None else None
	node.right = Node_Ext(src.right) if src.right != None else None

	extend_tree(node.left, src.left)
	extend_tree(node.right, src.right)


def update(node, k):
	if node == None:
		return '', '', 0

	li, lp, ld = update(node.left, k)
	ri, rp, rd = update(node.right, k)

	node.o_i = li + node.value + ri
	node.o_p = node.value + lp + rp
	node.d   = max(ld,rd) + 1

	if node.d == k:
		node.D[node.o_i + node.o_p] = 1

	if node.d > k:
		if node.left != None and node.left.d >= 2:
			for k in node.left.D.keys():
				if k in node.D.keys():
					node.D[k] += node.left.D[k]
				else:
					node.D[k] = node.left.D[k]

		if node.right != None and node.right.d >= 2:
			for k in node.right.D.keys():
				if k in node.D.keys():
					node.D[k] += node.right.D[k]
				else:
					node.D[k] = node.right.D[k]

	return node.o_i, node.o_p, node.d


def test():
	L, R = [], []
	in_order(root, L)
	pre_order(root, R)
	print(' ', L,'\n ',R)


	root_ext = Node_Ext(root)
	extend_tree(root_ext, root)

	L, R = [], []
	in_order(root_ext, L)
	pre_order(root_ext, R)
	print(' ', L,'\n ',R)

	update(root_ext, 2)
	view(root_ext)


def solve():
	root_ext = Node_Ext(root)
	extend_tree(root_ext, root)
	
	update(root_ext, 2)

	RD = root_ext.D
	r  = max(RD.values())
	if r >= 2:
		print('True')
		for k in RD.keys():
			if RD[k] >= 2:
				print([k, RD[k]])
	else:
		print('False')

	print('\n\n-----------------------')
	view(root_ext)


solve()