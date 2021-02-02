
# https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
#

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next  = next



def find_merge_point(head_1, head_2):
	m, n = length(head_1), length(head_2)

	if n > m:
		temp   = head_1
		head_1 = head_2
		head_2 = temp

	for i in range(int(abs(m-n))):
		head_1 = head_1.next

	while head_1 != None and head_2 != None:
		if head_1 == head_2:
			return head_1
		head_1 = head_1.next
		head_2 = head_2.next

	return None


def length(head):
	k = 0
	while head != None:
		head = head.next
		k += 1
	return k


def merge(start, src, k):
	prev = src
	for i in range(k):
		prev = prev.next
	
	start.next = prev


def print_list(head):
	curr = head
	while curr != None:
		print(curr.value)
		curr = curr.next
	print()
	return head


def load(L):
	head = Node(L[0])
	prev = head

	for i in range(1,len(L)):
		node = Node(L[i])
		prev.next = node
		prev = node

	return head, prev
	

def test():
	L1 = [1,2,3,4,5]
	L2 = [11,12]

	head_1, last_1 = load(L1)
	print_list(head_1)

	head_2, last_2 = load(L2)
	print_list(head_2)

	merge(last_2, head_1, 3)
	print_list(head_2)

	m, n = length(head_1), length(head_2)
	print(m, n)

	mp   = find_merge_point(head_1, head_2)
	v_mp = mp.value if mp != None else None
	print(mp, v_mp)

test()
