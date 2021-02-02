
# https://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/
#

class Node():
	
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


def find(node, value):
	if node is None:
		return None

	if value == node.value:
		return node

	elif value < node.value:
		return find(node.left, value)

	else:
		return find(node.right, value)


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


def is_equal(L1, L2):
	n1 = len(L1)
	n2 = len(L2)
	
	if n1 != n2:
		return False

	err = [1 for i in range(n1) if L1[i] != L2[i]]
	s   = sum(err)

	return True if s == 0 else False


def subtree(st_root, t_root):
	t_node = find(t_root, st_root.value)
	if t_node == None:
		return False

	for f_order in [in_order, pre_order]:
		T  = []
		ST = []
		
		f_order(t_node,  T)
		f_order(st_root, ST)

		if not is_equal(T, ST):
			return False

	return True




def sub_tree_rec(st_node, t_node):
	if st_node == None and t_node == None:
		return True

	elif st_node != None and t_node != None:
	
		if st_node.value != t_node.value:
			return False

		else:
			left  = sub_tree_rec(st_node.left,  t_node.left)
			right = sub_tree_rec(st_node.right, t_node.right)
			return left and right

	else:
		return False


def sub_tree(st_root, t_root):
	t_node = find(t_root, st_root.value)
	if t_node == None:
		return False
	else:
		return sub_tree_rec(st_root, t_node)



def show(fun, root, text):
	L = []
	fun(root, L)
	print(text, L)


def show_both(root):
	in_ord = []
	in_order(root, in_ord)

	pre_ord = []
	pre_order(root, pre_ord)

	print("In-Order :", in_ord)
	print("Pre-Order:", pre_ord)




def test():
	root = Node(3, Node(2, Node(1)),
				   Node(7, Node(5, Node(4), Node(6)), 
						   Node(8, None, 
								   Node(10, Node(9), Node(11)))))
	#st_root = Node(8, None,
	#				  Node(10, Node(9), Node(11)))

	st_root = Node(8, Node(7),
					  Node(10, Node(9), Node(11)))

	#st_root = Node(10, Node(9, Node(8)),
	#				   Node(11))


	show_both(find(root, st_root.value))
	show_both(st_root)
	
	res = subtree(st_root, root)
	print(res)

	res = sub_tree(st_root, root)
	print(res)


test()
