

def merge_sort(E):
	n = len(E)
	if n == 1:
		return E

	mid = int( n // 2 )

	L = merge_sort(E[:mid])
	R = merge_sort(E[mid:])

	n_L = len(L)
	n_R = len(R)

	S = []
	i = 0
	j = 0

	while i < n_L and j < n_R:
		if L[i][0] <= R[j][0]:
			S.append(L[i])
			i += 1
		else:
			S.append(R[j])
			j += 1

	if i == n_L:
		S = S + R[j:]
	
	if j == n_R:
		S = S + L[i:]

	return S


def test_merge_sort():
	L = [11,2,4,1,3,9,5,6,8,7,10]
	R = [(x, (x*10, x*20)) for x in L]
	S = merge_sort(R)

	for t in S:
		print(t)


#test_merge_sort()





# Data Structure
# Union by Rank and Path Compression
#
class Node():
	
	def __init__(self, data, rank=0, parent=None):
		self.rank   = rank
		self.parent = self if parent == None else parent
		self.data   = data


# path compression
def find_set(node):
	if node.parent == node:
		return node
	else:
		node.parent = find_set(node.parent)
	return node.parent


def link(n1, n2):
	if n1.rank < n2.rank:
		n1.parent = n2
	else:
		if n1.rank == n2.rank:
			n1.rank += 1
		n2.parent = n1


def union(n1, n2):
	r1 = find_set(n1)
	r2 = find_set(n2)
	link(r1, r2)




class Graph:

	def __init__(self, n, both_dir=True):
		self.n        = n
		self.adj      = {}
		self.both_dir = both_dir

		for i in range(n):
			self.adj[i] = {}

	
	def add_edge(self, u, v, w):
		self.adj[u][v] = w
		
		if self.both_dir:
			self.adj[v][u] = w


	def mst_kruskal(self):
		# Minimum Spanning Tree
		MST = []

		# Edges
		E = []
		for u in self.adj.keys():
			for v, w in self.adj[u].items():
				 E.append((w, (u, v)))
		
		# Sorted Edges by weight
		SE = merge_sort(E)

		# Vertices
		V  = [x for x in range(self.n)]
		# Used
		U  = [0 for x in V]
		# Union Set
		US = [Node(v) for v in V]
		
		# Added Vertices
		k = 0

		for w, (u,v) in SE:
			r_u = find_set(US[u])
			r_v = find_set(US[v])
			
			if r_u != r_v:
				union(r_u, r_v)
				MST.append((u,v,w))
				
				for z in [u,v]:
					if U[z] == 0:
						U[z] = 1
						k += 1

				if k == self.n:
					break

		return MST



def run():
	G = Graph(6, both_dir=False)

	G.add_edge(0,1,2)
	G.add_edge(0,2,1)

	G.add_edge(1,2,2)
	G.add_edge(1,3,3)

	G.add_edge(2,3,3)
	G.add_edge(2,4,1)

	G.add_edge(3,4,1)
	G.add_edge(3,5,5)

	G.add_edge(4,5,1)

	mst = G.mst_kruskal()
	m   = len(mst)	

	for i in range(m):
		print("Edge  :", mst[i])
	

run()
