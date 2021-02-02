
# https://www.geeksforgeeks.org/connect-leaves-doubly-linked-list/
#


class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


def convert_bt_dll(root, head):
	if root is None:
		return head

	prev = convert_bt_dll(root.left, head)
	
	node = Node(root.value)
	prev.right = node
	node.left  = prev
	
	return convert_bt_dll(root.right, node)
	

def test():	
	root = Node(8, Node( 4, Node(2, Node(1), Node(3)),
						    Node(6, Node(5), Node(7))),
				   Node(12, Node(10, Node(9), Node(11)), 
						    Node(14, Node(13), Node(15))) )

	head = Node("Head")

	convert_bt_dll(root, head)

	L = []
	curr = head
	L.append(curr.value)
	while curr.right != None:
		curr = curr.right
		L.append(curr.value)

	print()
	print(L)


	R = []
	R.append(curr.value)
	while curr.left != None:
		curr = curr.left
		R.append(curr.value)

	print()
	print(R)


test()