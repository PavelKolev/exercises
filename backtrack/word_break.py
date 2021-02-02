
# https://www.geeksforgeeks.org/word-break-problem-dp-32/
#





class Node():
	def __init__(self, value='', end=False, D={}):
		self.value = value
		self.end   = end
		self.D     = D


root = Node()

L = ['i', 'like', 'sam', 'sung', 'samsung',
	 'mobile', 'ice', 'cream', 'icecream',
	 'iceman', 'man', 'go', 'mango']

Q = 'icemanlikesamsung'


def view(node):
	if node.end == True:
		print(node.value)
	
	for k in node.D.keys():
		view(node.D[k])


def insert(node, word):
	curr = node
	for w in word:
		if not (w in curr.D.keys()):
			curr.D[w] = Node(curr.value + w, False, {})
		curr = curr.D[w]
	curr.end = True


def next_words(node, text, R):
	if text == '' or node.D == {}:
		return

	if not (text[0] in node.D.keys()):
		return

	next_node = node.D[text[0]]
	if next_node.end:
		R.append(next_node.value)

	next_words(next_node, text[1:], R)


def backtrack(root, Q):
	if Q == '':
		return True

	if root.D.keys() == {}:
		return False

	R = []
	next_words(root, Q, R)
	
	for word in R:
		n_i  = len(word)
		print(n_i, word, Q[n_i:])
 		res = backtrack(root, Q[n_i:])
		if res == True:
			return True

	return False


def load():
	for word in L:
		insert(root, word)


def test():
	load()
	view(root)
	print()

	R = []
	next_words(root, Q, R)
	for x in R:
		print(x)


def run_backtrack():
	load()
	res = backtrack(root, Q)
	print(res)


#test()
run_backtrack()
