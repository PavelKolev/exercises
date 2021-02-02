
# https://www.geeksforgeeks.org/word-break-problem-dp-32/
#



class Node():
	def __init__(self, value='', end=False, D={}):
		self.value = value
		self.end   = end
		self.D     = D


root = Node()

L = ['and', 'cream', 'go', 'i', 'ice',
	 'like', 'mobile', 'man', 'mango'
	 'sam', 'sung', 'samsung']

Q = 'icemanlikesamsungiice'

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


def dyn_prog(node, Q):
	n = len(Q)
	T = [0 for i in range(n)]

	first_symbols = list(node.D.keys())

	T[n-1] = 1 if Q[n-1] in first_symbols and node.D[Q[n-1]].end else 0

	for i in reversed(range(n-1)):
		is_Qi_symbol = Q[i] in first_symbols
		
		if not is_Qi_symbol:
			T[i] = 0

		# is_Qi_symbol == True
		elif node.D[Q[i]].end and T[i+1] == 1:
			T[i] = 1
			print(i, Q[i], n)
			continue

		# is_Qi_symbol == True and 
		# ((node.D[Q[i]].end == False and T[i+1] == 1) or
		#  (node.D[Q[i]].end == True  and T[i+1] == 0) or
		#  (node.D[Q[i]].end == False and T[i+1] == 0) )
		#
		else:
			next_node = node.D[Q[i]]
			W = []
			next_words(next_node, Q[i+1:], W)

			success = False
			for word in W:
				n_w = len(word)
				print(i, n_w, word, n)
				if i + n_w == n or T[i + n_w] == 1:
					success = True
					break

			T[i] = 1 if success else 0

	return T


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


def run_dp():
	load()

	T = ["ilikesamsung", "iiiiiiii", "ilikelikeimangoiii",
		 "samsungandmango", "samsungandmangok"]

	#T = [Q]

	for word in T:
		res = dyn_prog(root, word)

		line = '['
		for w in word[:-1]:
			line += w + ', '
		line += word[-1] + ']'

		print(line)
		print(res)
		print('True' if res[0] == 1 else 'False')
		print()
		

#test()
run_dp()

