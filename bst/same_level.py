
# https://www.geeksforgeeks.org/connect-nodes-at-same-level/
#


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


class Node_Ext:
	def __init__(self, value, left=None, right=None, next_node=None):
		self.value = value
		self.left  = left
		self.right = right

		self.next_right = next_node



root = Node('A', Node('B', Node('D'), Node('E')),
				 Node('C', None, Node('F')))

# Input Tree
#        A
#       / \
#      B   C
#     / \   \
#    D   E   F


# Output Tree
#        A--->None
#       / \
#      B-->C-->None
#     / \   \
#    D-->E-->F-->None


def solve(node, k, D):
	if node == None:
		return None

	left_ext = solve(node.left, k+1, D)
	right_ext = solve(node.right, k+1, D)

	ext_node = Node_Ext(node.value, left_ext, right_ext)

	if k not in D.keys():
		D[k] = ext_node
	else:
		# Update Next Right
		D[k].next_right = ext_node
		
		# Insert Next Right
		D[k] = ext_node

	return ext_node



def pre_order(node):
	if node == None:
		return None

	print(node.value)
	pre_order(node.left)
	pre_order(node.right)


def view(node):
	if node == None:
		return

	curr = node
	while curr != None:
		print(curr.value)
		curr = curr.next_right

	view(node.left)


def run():
	D = {}
	ext_root = solve(root, 0, D)

	pre_order(ext_root)
	print()
	view(ext_root)


run()