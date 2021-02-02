




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


def remove(p, node, d, k):
	if node is None:
		return d-1

	d_l = remove(node, node.left,  d+1, k)
	d_r = remove(node, node.right, d+1, k)
	m_d = max(d_l, d_r)

	if node.left is None and node.right is None:
		if m_d <= k:
			if p.left == node:
				p.left  = None
			else: #p.right == node
				p.right = None

	return m_d
	

def test():
	root = Node(-1, Node(12, Node(1)),
					Node(10, Node(2, Node(20), Node(2)), 
							 Node(10, None, 
								 	  Node(-25, Node(3), Node(4)))))
	head = Node(-111)
	head.right = root
	
	L = []
	show_in_order(head, L)
	print(L[1:])
	
	k = 3
	remove(head, root, 0, k)

	L = []
	show_in_order(head, L)
	print("with k=", k)
	print(L[1:])

test()