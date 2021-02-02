
import heapq as pq

class Graph:
	def __init__(self, n):
		self.n   = n
		self.adj = {}
		
		for i in range(n):
			self.adj[i] = {}

	def add_edge(self, u, v, w):
		self.adj[u][v] = w
		self.adj[v][u] = w


	def dijkstra(self, s):
		N = self.n
		A = self.adj

		visited = [False] * N
		prev    = [-1] * N
		
		dist    = [float('infinity')] * N
		dist[s] = 0

		Q = [(dist[s], s)]
		while Q:
			_, u = pq.heappop(Q)
			visited[u] = True

			for v in A[u].keys():
				if visited[v]:
					continue

				new_dv = dist[u] + A[u][v]
				if new_dv < dist[v]:
					dist[v] = new_dv
					prev[v] = u
					pq.heappush(Q, (new_dv, v))

		return dist, prev


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

	dist, prev = G.dijkstra(0)
	
	print("Vertices  :", list(range(6)))
	print("Distances :", dist)
	print("Previous  :", prev)

run()



def	test():
	pq = [ (4,'E'), (3,'D'), (1,'B'), (2,'C'), (0, 'A') ]
	#pq = [ 4, 3, 1, 2, 0]
	print(pq)

	heapq.heapify(pq)
	print(pq)

	q = heapq.heappop(pq)
	print(q)
	print(pq)

	heapq.heappush(pq, (0,'Q'))
	print(pq)

#test()
