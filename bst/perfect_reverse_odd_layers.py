

# https://www.geeksforgeeks.org/reverse-alternate-levels-binary-tree/
#

from collections import defaultdict

class Node():

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


def read_in_order_left(node, k, Q):
	if node is None:
		return

	read_in_order_left(node.left, k+1, Q)
	
	if k % 2 == 1:
		Q[k].append(node.value)

	read_in_order_left(node.right, k+1, Q)


def write_in_order_right(node, k, Q):
	if node is None:
		return

	write_in_order_right(node.right, k+1, Q)

	if k % 2 == 1:
		q = Q[k].pop(0)
		node.value = q

	write_in_order_right(node.left, k+1, Q)


def rev_odd(root):
	Q = defaultdict(list)
	read_in_order_left(root, 0, Q)
	write_in_order_right(root, 0, Q)


def bfs(root):
	Q = [(0, root)]
	D = defaultdict(list)
	k = 0
	
	while Q:
		k, node = Q.pop(0)

		D[k].append((k, node.value))
		
		N = [node.left, node.right]
		for n in N:
			if n is not None:
				Q.append((k+1, n))

	return D


def test():
	root = Node(8, Node(4, Node(2, Node(1), Node(3)),
						   Node(6, Node(5), Node(7))),
				   Node(12, Node(10, Node(9), Node(11)), 
						    Node(14, Node(13), Node(15))) )

	Q = bfs(root)
	for k in Q.keys():
		print([y for x,y in Q[k]])

	rev_odd(root)
	print()

	Q = bfs(root)
	for k in Q.keys():
		print([y for x,y in Q[k]])


test()
