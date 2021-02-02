
# https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/
#


def dynamic(G):
	n = len(G)
	A = [[([],[]) for j in range(n)] for i in range(n) ]

	# Two initial conditions !!!
	#
	A[0] = [([x],[]) for x in G]
	A[1] = [([max(x,y)],[min(x,y)]) for x,y in zip(G[:-1],G[1:])]
	
	for i in range(2,n):
		for j in range(n-i):
			
			c_L = A[0][ j ][0] + A[i-1][j+1][1]
			c_R = A[0][j+i][0] + A[i-1][ j ][1]

			if sum(c_L) > sum(c_R):
				A[i][j] = (c_L, A[i-1][j+1][0])
			else:
				A[i][j] = (c_R, A[i-1][j][0])
	
	return A




# Recursive Solution
#
def game(G, F=[], S=[], k=0):
	if G == []:
		return F, S

	if k % 2 == 0:
		# First player moves
		lF = F.copy()
		lF.append(G[0])
		lG = G[1:].copy()

		lF, lS = game(lG, lF, S, k+1)
		#print(1, lF, lS, k)

		rF = F.copy()
		rF.append(G[-1])
		rG = G[:-1].copy()

		rF, rS = game(rG, rF, S, k+1)
		#print(2, rF, rS, k)

		if sum(lF) > sum(rF):
			return lF, lS  
		else:
			return rF, rS

	else:
		# Second players moves
		lS = S.copy()
		lS.append(G[0])
		lG = G[1:].copy()

		lF, lS = game(lG, F, lS, k+1)
		#print(3, lF, lS, k)

		rS = S.copy()
		rS.append(G[-1])
		rG = G[:-1].copy()

		rF, rS = game(rG, F, rS, k+1)
		#print(4, rF, rS, k)

		if sum(lS) > sum(rS):
			return lF, lS
		else:
			return rF, rS



def test():
	#G = [5,3,7,10]
	G = [9,11,10,7,21,22]

	F, S = game(G)

	print("Game:          ", G)
	print("First  Player: ", F, sum(F))
	print("Second Player: ", S, sum(S))
	print()

	A = dynamic(G)
	n = len(G)
	for i in range(n):
		print(A[i][:n-i])

# RUN
test()

