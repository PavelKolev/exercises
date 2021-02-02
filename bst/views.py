
# https://www.geeksforgeeks.org/print-left-view-binary-tree/
# https://www.geeksforgeeks.org/bottom-view-binary-tree/
#


class Node():
	
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


def bottom_view(node, h, D):
	if node == None:
		return

	D[h] = node.value
	bottom_view(node.left,  h-1, D)
	bottom_view(node.right, h+1, D)


def left_view(node, v, D):
	if node == None:
		return

	D[v] = node.value
	left_view(node.right, v+1, D)
	left_view(node.left, v+1, D)


def test_bottom(root):
	D = {}
	bottom_view(root, 0, D)
	
	m = min(D.keys())
	M = max(D.keys())
	L = [D[i] for i in range(m,M+1) if D[i] != None]
	print("Bottom View: ", L)


def test_left(root):
	D = {}
	left_view(root, 0, D)
	
	M = max(D.keys())
	L = [D[i] for i in range(0,M+1) if D[i] != None]
	print("Left View: ", L)
	

def test():
	root = Node(-1, Node(12),
					Node(10, Node(2, Node(20), Node(2)), 
							 Node(10, None, 
								 	  Node(-25, Node(3), Node(4)))))

	BV = test_bottom(root)
	LV = test_left(root)

test()