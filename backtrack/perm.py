
#https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
#

import math



def perm(S, w, L):
	if S == '':
		L.append(w)
		return

	n = len(S)
	for i in range(n):
		s = S[i]
		Z = ''

		if i == 0:
			Z = S[i+1:]
		elif i == n-1:
			Z = S[:i]
		else:
			Z = S[:i] + S[i+1:]

		perm(Z, w + s, L)



def test():
	S = 'ABCD'
	L = []
	perm(S, '', L)

	n = len(L)
	N = math.factorial(len(S))
	print(n, N, '\n')

	for i in range(len(L)):
		print(L[i])


test()