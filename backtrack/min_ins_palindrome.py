
# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
#


# abcde
# bcde, abcd

# aeqqe
# eaeqqe -> aeqq
# aeqqea -> eqqe

S = ['aeqqe', 'ab', 'aa', 'abcd', 'abcda', 'abcde']


def dyn_prog(S, n):
	D = [[0 for i in range(n+1-i)] for i in range(n+1)]

	for j in range(n):
		D[1][j] = 1

	for j in range(n-1):
		D[2][j] = 0 if S[j] == S[j+1] else 1

	for i in range(3,n+1):
		for j in range(n+1-i):
			
			if S[j] == S[j+i-1]:
				D[i][j] = D[i-2][j+1]

			else:
				D[i][j] = 1 + min( D[i-1][j], D[i-1][j+1] )

	return D


def backtrack(S, n):
	if n <= 1:
		return n

	if n == 2:
		return 0 if S[0] == S[1] else 1

	# n >= 3
	if S[0] == S[-1]:
		return backtrack(S[1:-1], n-2)
	
	else:
		l = backtrack(S[1:],  n-1)
		r = backtrack(S[:-1], n-1)
		return 1 + min(l,r)


def test_backtrack():
	for w in S:
		print(w, backtrack(w, len(w)))


def test_dynamic_programming():
	S = 'aeqqe'
	n = len(S)

	D = dyn_prog(S, n)

	for x in range(n+1):
		print(D[x])



#test_backtrack()
test_dynamic_programming()

