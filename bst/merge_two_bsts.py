


# https://www.geeksforgeeks.org/merge-two-bsts-with-limited-extra-space/
#


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


r1 = Node(4, Node(2, Node(1), Node(3)),
			 Node(6, Node(5), Node(7)))

r2 = Node(11, Node(9,   Node(8), Node(10)),
			  Node(13, Node(12), Node(14)))

r2 = Node(8,  Node(6,   Node(5), Node(7)),
			  Node(10,  Node(9), Node(11)))


def in_order(node):
	if node == None:
		return

	in_order(node.left)
	print(node.value)
	in_order(node.right)


def merge_bst(node_1, node_2):
	S1, S2 = [node_1], [node_2]
	d1, d2 = True, True

	while S1 != [] and S2 != []:
		n1 = S1[0]
		if d1:
			if n1.left != None:
				S1.insert(0, n1.left)
				d1 = True
			else:
				d1 = False

		n2 = S2[0]
		if d2:
			if n2.left != None:
				S2.insert(0, n2.left)
				d2 = True
			else:
				d2 = False

		if not d1 and not d2:
			if n1.value <= n2.value:
				print(n1.value)
				S1.pop(0)

				if n1.right != None:
					S1.insert(0, n1.right)
					d1 = True

			else:
				print(n2.value)
				S2.pop(0)

				if n2.right != None:
					S2.insert(0, n2.right)
					d2 = True

	Z = S1 if S1 != [] else S2
	d = d1 if S1 != [] else d2

	while Z != []:
		node = Z[0]
		if d:
			if node.left != None:
				Z.insert(0, node.left)
				d = True
			else:
				d = False
		else:
			print(node.value)
			Z.pop(0)

			if node.right != None:
				Z.insert(0, node.right)
				d = True




def test():
	in_order(r1)
	print()

	in_order(r2)
	print()

	merge_bst(r1, r2)


test()
