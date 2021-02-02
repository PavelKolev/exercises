



# https://www.geeksforgeeks.org/topological-sorting/
#


class Graph:
	def __init__(self, n):
		self.n   = n
		self.adj = {}
		
		for i in range(n):
			self.adj[i] = []

	def add_edge(self, u, v):
		self.adj[u].append(v)


	def topological_sort(self):
		N = self.n
		A = self.adj

		layer   = [0] * N
		visited = [False] * N
		in_deg  = [0] * N

		for u in range(N):
			for v in A[u]:
				in_deg[v] += 1

		Q = []
		for u in range(N):
			if in_deg[u] == 0:
				Q.append(u)
		
		while Q:
			u = Q.pop(0)
			visited[u] = 1
			print("Layer ", layer[u], "Vertex ", u)

			for v in A[u]:
				in_deg[v] -= 1
				if in_deg[v] == 0 and visited[v] == 0:
					Q.append(v)
					layer[v] = layer[u] + 1
	

def test_topological_sort():
	G = Graph(7)

	G.add_edge(0,5)
	G.add_edge(1,5)
	G.add_edge(1,2)
	#G.add_edge(2,4)
	G.add_edge(2,5)
	G.add_edge(3,2)
	G.add_edge(3,4)
	G.add_edge(4,5)
	G.add_edge(5,6)

	#G = Graph(6)
	#G.add_edge(5, 2) 
	#G.add_edge(5, 0) 
	#G.add_edge(4, 0) 
	#G.add_edge(4, 1) 
	#G.add_edge(2, 3) 
	#G.add_edge(3, 1) 

	G.topological_sort()


test_topological_sort()