
# Count BST nodes that lie in a given range
# https://www.geeksforgeeks.org/count-bst-nodes-that-are-in-a-given-range/
#




class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right


R    = [5,45]
root = Node(10, Node(5, Node(1)),
				Node(50, Node(40), Node(100)))

def solve(node, R):
	if node == None:
		return 0

	S = []

	if R[0] <= node.value and\
		node.value <= R[1]:
		S.append(1)
	
	if R[0] < node.value:
		s = solve(node.left, R)
		S.append(s)

	if R[1] > node.value:
		s = solve(node.right, R)
		S.append(s)

	return sum(S)


def run():
	r = solve(root, R)
	print(r)		


run()



