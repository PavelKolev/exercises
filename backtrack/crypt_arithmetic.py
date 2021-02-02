
# https://www.geeksforgeeks.org/solving-cryptarithmetic-puzzles-backtracking-8/
#




import numpy as np


A =  'SEND'
#   +
B =  'MORE'
#----------
C = 'MONEY'




def decrypt(A, B, C, D, K, N):
	n_K = len(K)
	n_N = len(N)

	if n_K == 0:
		if check(A,B,C,D):
			for k in D.keys():
				print(k, D[k])
			print()
		return

	k = next(iter(K))
	
	for n in N:
		NN = N.copy()
		NN.remove(n)

		KK = K.copy()
		KK.remove(k)
	
		D[k] = n

		decrypt(A, B, C, D, KK, NN)


def check(A,B,C,D):
	x = int(''.join([str(D[a]) for a in A]))
	y = int(''.join([str(D[b]) for b in B]))
	z = int(''.join([str(D[c]) for c in C]))

	return z == x + y


def split(A):
	return [x for x in A]


def test():
	Q = np.unique(split(A) + split(B) + split(C))
	D = {q:-1 for q in Q}
	n = len(D)
	
	N = set(range(0,10))
	K = set(D.keys())

	decrypt(A, B, C, D, K, N)
	

test()
