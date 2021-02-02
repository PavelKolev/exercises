
# https://www.geeksforgeeks.org/solving-cryptarithmetic-puzzles-backtracking-8/
#



A = '$SEND'
#   +
B = '$MORE'
#----------
C = 'MONEY'


A = '$$TO'
#   +
B = '$$GO'
#----------
C = '$OUT'




def decrypt(W, D, N, c, i, j, n):
	if j == n:
		for k in D.keys():
			print(k, D[k])
		print()
		return
	
	if i == 0 or i == 1:
		if W[i][j] == '$':
			decrypt(W, D, N, c, i+1, j, n)

		else: # W[i][j] != '$'

			if D[W[i][j]] != -1:
				decrypt(W, D, N, c, i+1, j, n)

			else: # D[W[i][j]] == -1
				for num in N:
					NN = N.copy()
					NN.remove(num)
					
					x = D[W[i][j]]
					D[W[i][j]] = num

					decrypt(W, D, NN, c, i+1, j, n)

					D[W[i][j]] = x


	if i == 2:
		x   = D[W[0][j]] if W[0][j] != '$' else 0
		y   = D[W[1][j]] if W[1][j] != '$' else 0
		res = x + y + c

		if W[2][j] == '$':
			
			if 0 == res % 10:
				decrypt(W, D, N, res//10, 0, j+1, n)
			else:
				return
		
		else: #W[2][j] != '$'
			if D[W[2][j]] != -1:

				if D[W[2][j]] == res % 10:
					decrypt(W, D, N, res//10, 0, j+1, n)

			else: #D[W[2][j]] == -1:
				for num in N:
					if num == res % 10:
						NN = N.copy()
						NN.remove(num)
						
						x = D[W[2][j]]
						D[W[2][j]] = num

						decrypt(W, D, NN, res//10, 0, j+1, n)

						D[W[2][j]] = x

			
def split(A):
	return [x for x in A]


def test():
	Q = set(split(A) + split(B) + split(C))
	Q.remove('$')

	W = [A[::-1], B[::-1], C[::-1]]
	D = {q:-1 for q in Q}
	N = set(range(0,10))
	
	decrypt(W, D, N, 0, 0, 0, len(W[0]))
	

test()














