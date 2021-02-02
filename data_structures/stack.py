
# Implement Stack
#

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next  = next


class Stack:
	def __init__(self):
		self.head = Node('Head')
		self.size = 0

	def push(self, x):
		node = Node(x)

		if self.head.next == None:
			self.head.next = Node(x)
		else:
			next_node = self.head.next
			self.head.next = Node(x, next_node)

		self.size += 1

	def pop(self):
		top = self.head.next
		if top == None:
			return None

		self.head.next = top.next
		self.size -= 1
		return top.value

	def top(self):
		node = self.head.next
		return None if node == None else node.value

	def is_empty(self):
		return True if self.size == 0 else False


def test():
	S = Stack()

	for i in range(5):
		S.push(i)

	while not S.is_empty():
		x = S.pop()
		print(x)


def parse(input):
	br    = {')': '(', ']':'[', '}':'{'}
	left  = "{[("
	right = ")]}"

	S = Stack()

	for x in input:
		#print(x)
		if left.find(x) != -1:
			S.push(x)
			#print('push ', x)

		if right.find(x) != -1:
			if S.top() != br[x]:
				return False
			y = S.pop()

	return S.is_empty()


res = parse("{(1,2)[x][22]}")
print(res)
