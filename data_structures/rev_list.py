
# https://www.geeksforgeeks.org/reverse-a-linked-list/
#

class Node:
	data = 0
	next = None

	def __init__(self, data, next):
		self.data = data
		self.next = next


l3   = Node(4, None)
l2   = Node(3, l3)
l1   = Node(2, l2)
head = Node(1, l1)


def show(node):
	while node != None:
		print(node.data)
		node = node.next


def show_reverse(node):
	if node == None:
		return
	show_reverse(node.next)
	print(node.data)


def reverse(node):
	prev_node = None

	while node != None:
		next_node = node.next
		node.next = prev_node
		prev_node = node
		node      = next_node

	return prev_node


def rev_list(prev, curr):
	if curr.next == None:
		curr.next = prev
		return curr

	head = rev_list(curr, curr.next)
	curr.next = prev
	return head


show(head)
print()

rev_head = reverse(head)
show(rev_head)
print()

head = reverse(rev_head)
show(head)
print()

# Recursive Calls
show_reverse(head)
print()

rev_head_v2 = rev_list(None, head)
show(rev_head_v2)
print()
