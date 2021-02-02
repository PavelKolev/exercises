
# https://www.geeksforgeeks.org/binary-search-tree-data-structure/
#

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left  = left
		self.right = right
		
# Simplest
def in_order(node, L):
	if node == None:
		return

	in_order(node.left, L)
	L.append(node.value)
	in_order(node.right, L)


def is_sorted(L):
	for i in range(len(L)-1):
		if L[i] > L[i+1]:
			return False
	return True


def is_BST(node):
	L = []
	in_order(node, L)
	print(L)
	return is_sorted(L)


# Elegant Solution
def is_BST(node, lb, ub):
	if node == None:
		return True

	if lb <= node.value and node.value <= ub and\
	   is_BST(node.left, lb, node.value) and\
	   is_BST(node.right, node.value, ub):
		return True
	else:
		return False


# Recursion with external memory (L,R)
def in_order_LB(node, L, R):
	if node == None:
		return

	in_order_LB(node.left, L, R)
	
	if R[0] == False:
		return
	elif L[0] <= node.value:
		L[0] = node.value
	else:
		R[0] = False
		R[1] = node.value
		return
		
	in_order_LB(node.right, L, R)




def height(root):
	if root == None:
		return -1

	l_H = height(root.left)
	r_H = height(root.right)

	return 1 + max(l_H, r_H)


def find_height(root, height=0):
	# No children
	if root.left == None and root.right == None:
		return height

	# Two children
	elif root.left != None and root.right != None:
		return 1 + max(find_height(root.left, height), find_height(root.right, height))

	# Only left child
	elif root.left != None:
		return find_height(root.left, height+1)

	# Only right child
	else:
		return find_height(root.right, height+1)



# Level traversal or BST
def BFS(root):
	if root == None:
		return

	Q = [root]
	while Q:
		node = Q.pop(0)
		print(node.value)
		
		if node.left != None:
			Q.append(node.left)

		if node.right != None:
			Q.append(node.right)


def DFS(root):
	if root == None:
		return

	print(root.value)
	DFS(root.left)
	DFS(root.right)




def test_BST():
	lb = 0
	ub = 100
	L  = [lb]
	R  = [True, -1]

	root = Node(8, Node(3, Node(2), Node(5, Node(4), Node(6))),
				   Node(10, Node(9), Node(11)) )

	in_order_LB(root, L, R)
	print(R)

	print("BST Height: ", find_height(root))
	print("BST Height: ", height(root))

	BFS(root)
	print()
	DFS(root)

test_BST()