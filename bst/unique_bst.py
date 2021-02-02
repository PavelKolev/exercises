

# https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
#


class Node():
	
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


def in_order(node, L):
	if node is None:
		return

	in_order(node.left, L)
	L.append(node.value)
	in_order(node.right, L)


def pre_order(node, L):
	if node is None:
		return

	L.append(node.value)
	pre_order(node.left, L)
	pre_order(node.right, L)


def show(fun, root, text):
	L = []
	fun(root, L)
	print(text, L)



def unique(in_ord, pre_ord):
	if in_ord == []:
		return None

	value = pre_ord.pop(0)
	idx   = [i for i,x in enumerate(in_ord) if x == value][0]
	n     = len(in_ord)
	
	L = in_ord[:idx]   if idx>=0   else []
	R = in_ord[idx+1:] if idx<=n-2 else []

	node       = Node(value)
	node.left  = unique(L, pre_ord)
	node.right = unique(R, pre_ord)

	return node

	
def test():
	root = Node(3, Node(2, Node(1)),
				   Node(7, Node(5, Node(4), Node(6)), 
						   Node(8, None, 
								   Node(10, Node(9), Node(11)))))
	
	in_ord = []
	in_order(root, in_ord)

	pre_ord = []
	pre_order(root, pre_ord)

	#in_ord  = ['D','B','E','A','F','C']
	#pre_ord = ['A','B','D','E','C','F']

	print("In-Order :", in_ord)
	print("Pre-Order:", pre_ord)

	root = unique(in_ord, pre_ord)
	
	print()
	show(in_order,  root, "In-Order :")
	show(pre_order, root, "Pre-Order:")


test()
