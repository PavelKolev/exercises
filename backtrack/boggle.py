
# https://www.geeksforgeeks.org/boggle-set-2-using-trie/
#

import numpy as np


W = ["GEEKS", "FOR", "QUIZ", "GO"]
T = [['G', 'I', 'Z'],
	 ['U', 'E', 'K'],
  	 ['Q', 'S', 'E']]

W = ["GEEKS", "ABCFIHGDE"]
T = [['A', 'B', 'C'],
	 ['D', 'E', 'F'],
	 ['G', 'H', 'I']]

W = ['a', 'b', 'e', 'f', 'i', 'l', 'm', 'o', 's', 't',
	 'u', 'w', 'x', 'ae', 'am', 'as', 'aw', 'ax', 'bo',
	 'bu', 'ea', 'el', 'em', 'es', 'fa', 'ie', 'io', 'li',
	 'lo', 'ma', 'me', 'mi', 'oe', 'ox', 'sa', 'se', 'st',
	 'tu', 'ut', 'wa', 'we', 'xi', 'aes', 'ame', 'ami',
	 'ase', 'ast', 'awa', 'awe', 'awl', 'blo', 'but', 'elb',
	 'elm', 'fae', 'fam', 'lei', 'lie', 'lim', 'lob', 'lox',
	 'mae', 'maw', 'mew', 'mil', 'mix', 'oil', 'olm', 'saw',
	 'sea', 'sew', 'swa', 'tub', 'tux', 'twa', 'wae', 'was',
	 'wax', 'wem', 'ambo', 'amil', 'amli', 'asem', 'axil',
	 'axle', 'bleo', 'boil', 'bole', 'east', 'fame', 'limb',
	 'lime', 'mesa', 'mewl', 'mile', 'milo', 'oime', 'sawt',
	 'seam', 'seax', 'semi', 'stub', 'swam', 'twae', 'twas',
	 'wame', 'wase', 'wast', 'weam', 'west', 'amble', 'awest',
	 'axile', 'embox', 'limbo', 'limes', 'swami', 'embole',
	 'famble', 'semble', 'wamble']
W = [w.upper() for w in W]
T = [['F', 'X', 'I', 'E'],
	 ['A', 'M', 'L', 'O'],
	 ['E', 'W', 'B', 'X'],
	 ['A', 'S', 'T', 'U']]



class Node():
	def __init__(self, value, end, D):
		self.value = value
		self.end   = end
		self.D     = D


root = Node('', False, {})


def insert(node, word):
	curr = node

	for w in word:
		if not (w in curr.D.keys()):
			curr.D[w] = Node(curr.value + w, False, {})
		curr = curr.D[w]

	curr.end = True
	

def view(node):
	for k in node.D.keys():
		if node.D[k].end:
			print(node.D[k].value)
		view(node.D[k])


def load():
	for word in W:
		insert(root, word)


def adj(i,j,m,n):
	N = [(i-1,j-1), (i-1,j), (i-1,j+1),
		 (i,j-1), (i,j+1),
		 (i+1,j-1), (i+1,j), (i+1,j+1)]

	R = [(i,j) for i,j in N if i>=0 and i<=m-1 
							and j>=0 and j<=n-1]
	return R


def find_words(node, U, i, j, m, n, R):
	if (i,j) in U:
		return

	if not (T[i][j] in node.D.keys()):
		return

	U.add((i,j))

	if node.D[T[i][j]].end:
		R.append(node.D[T[i][j]].value)

	# Explore available neighbours
	#
	N  = adj(i, j, m, n)
	AN = [(x,y) for x,y in N if not ((x,y) in U)]
	
	node = node.D[T[i][j]]
	for x, y in AN:
		find_words(node, U, x, y, m, n, R)

	U.remove((i,j))


def solve():
	m = len(T)
	n = len(T[0])
	R = []

	for i in range(m):
		for j in range(n):
			U = set()
			C = []
			
			find_words(root, U, i, j, m, n, C)
			
			if C != []:
				R += [[(i,j), C]]

	return R


def test():
	load()
	#view(root)
	#print()

	for l in T:
		print(l)
	print()

	R = solve()
	for word in R:
		print(word)

	print()
	Q = []
	for w in R:
		Q = list(np.unique(Q + w[1]))
	print( [len(W), len(Q)] )


test()

			


