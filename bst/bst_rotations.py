

class Node:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value  = value
		self.left   = left
		self.right  = right
		self.parent = parent

		self.height       = 1
		self.left_height  = 0
		self.right_height = 0


def in_order(node, L):
	if node == None:
		return

	in_order(node.left, L)
	L.append((node.value, node.height))
	in_order(node.right, L)


def pre_order(node, L):
	if node == None:
		return

	L.append((node.value, node.height))
	pre_order(node.left, L)
	pre_order(node.right, L)


def build_bst(head, L):
	root = Node(L[0], None, None, head)
	head.right = root

	print(L)
	print()

	for value in L[1:]:
		root = head.right
		insert_node(head, root, value)
		balance(head, head, head.right, value)
		print_data(value, head, L)
	

def print_data(value, head, L):
	print(value)

	L = []
	in_order(head, L)
	print(L)
	
	L = []
	pre_order(head, L)
	print(L)

	print()


def insert_node(prev, curr, value):
	if curr == None:
		if prev.value < value:
			prev.right        = Node(value, None, None, prev)
			prev.right_height = 1
		else:
			prev.left 		  = Node(value, None, None, prev)
			prev.left_height  = 1
		prev.height = 1 + max(prev.left_height, prev.right_height)
		return

	if value < curr.value:
		insert_node(curr, curr.left, value)
	else:
		insert_node(curr, curr.right, value)
	
	if prev.left == curr:
		prev.left_height  = curr.height
	else:
		prev.right_height = curr.height
	prev.height = 1 + max( prev.left_height, prev.right_height )


def balance(head, prev, curr, value):
	if curr.value == value:
		return prev

	if value < curr.value:
		new_curr = balance(head, curr, curr.left, value)
	else:
		new_curr = balance(head, curr, curr.right, value)

	if prev == head:
		return None
	
	if abs(prev.left_height - prev.right_height) <= 2:
		return prev		

	if prev.left_height > prev.right_height:
		new_parent = right_rotation(prev, new_curr)
	else:
		new_parent = left_rotation(prev, new_curr)

	return new_parent


# Right Rotation
#
# parent               parent
#        prev     ->          curr
#   curr      b             x      prev
# x     z                        z      b
def right_rotation(prev, curr):
	curr_right_height = curr.right_height
	prev_left_height  = prev.left_height

	parent = prev.parent
	prev_is_left = True if parent.left == prev else False

	if prev_is_left:
		parent.left = curr
	else:
		parent.right = curr
	curr.paren = parent

	prev.parent = curr
	prev.left   = curr.right
	
	if curr.right != None:
		curr.right.parent = prev
	curr.right = prev

	# update height
	prev.left_height  = curr_right_height
	prev.height       = 1 + max( prev.left_height, prev.right_height )

	curr.right_height = prev.height
	curr.height       = 1 + max( curr.left_height, curr.right_height )

	if prev_is_left:
		parent.left_height  = curr.height
	else:
		parent.right_height = curr.height
	parent.height = 1 + max( parent.left_height, parent.right_height )
	
	
	return curr


# Left Rotation
#
# parent 				    parent
#        prev          ->          curr
#     x       curr            prev      b
#           z      b        x     z
#
def left_rotation(prev, curr):
	curr_left_height  = curr.left_height
	prev_right_height = prev.right_height

	parent = prev.parent
	prev_is_left = True if parent.left == prev else False

	if prev_is_left:
		parent.left = curr
	else:
		parent.right = curr
	curr.parent = parent

	prev.parent = curr
	prev.right  = curr.left

	if curr.left != None:
		curr.left.parent = prev
	curr.left = prev

	# update height
	prev.right_height = curr_left_height
	prev.height       = 1 + max( prev.left_height, prev.right_height )

	curr.left_height  = prev.height
	curr.height       = 1 + max( curr.left_height, curr.right_height )

	if prev_is_left:
		parent.left_height  = curr.height
	else:
		parent.right_height = curr.height
	parent.height = 1 + max( parent.left_height, parent.right_height )

	return curr


def test():
	head = Node(-1)
	L    = [34, 8, 10, 3, 2, 80, 30, 33, 1]
	
	build_bst(head, L)


test()



