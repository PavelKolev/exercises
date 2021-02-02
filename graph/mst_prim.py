

import heapq as pq


class Graph:
	def __init__(self, n):
		self.n        = n
		self.adj      = {}

		for i in range(n):
			self.adj[i] = {}

	
	def add_edge(self, u, v, w):
		self.adj[u][v] = w
		self.adj[v][u] = w


	def mst_prim(self):
		U = [0 for i in range(self.n)]
		
		#Set Initial Vertex 
		s    = 0
		U[s] = 1

		# Min Priority Queue
		# Initialize with Edges of (0,v) in E
		Q = []
		for v, w in self.adj[s].items():
			pq.heappush(Q, (w, (s,v)))

		MST = []
		for _ in range(self.n - 1):
			w_uv, (u,v) = pq.heappop(Q)
			MST.append((u,v))
			U[v] = 1

			for z, w_vz in self.adj[v].items():
				if U[z] == 0:
					pq.heappush(Q, (w_vz, (v,z)))

		return MST


def run():
	G = Graph(6)

	G.add_edge(0,1,2)
	G.add_edge(0,2,1)

	G.add_edge(1,2,2)
	G.add_edge(1,3,3)

	G.add_edge(2,3,3)
	G.add_edge(2,4,1)

	G.add_edge(3,4,1)
	G.add_edge(3,5,5)

	G.add_edge(4,5,1)

	mst = G.mst_prim()
	m   = len(mst)	

	for i in range(m):
		print("Edge  :", mst[i])
	

run()
