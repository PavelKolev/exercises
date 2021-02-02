


# Matrix Chain Multiplication | DP-8
# https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/
#


def mtx_mult(M):
	n = len(M)

	B = [0 for i in range(n)]
	D = [0 for i in range(n)]

	D[1] = M[0][0] * M[0][1] * M[1][1]

	for i in range(2,n):
		block = D[i-1] + M[0][0]   * M[i-1][1] * M[i][1]
		lastM = D[i-2] + M[i-1][0] * M[i-1][1] * M[i][1]

		B[i] = 1 if block < lastM else 0
		D[i] = min(block, lastM)

	return D, B


def show(M, B, i, n):
	if i <= 0:
		return ''

	if B[i] == 1:
		res = show(M, B, i-1, n)
		R = '[' + res + '] * ' + str_T(M[i])

	else:
		res = show(M, B, i-2, n)
		if res == '':
			R = str_T(M[i-1]) + ' * ' + str_T(M[i])
		else:
			R = '[' + res + '] * [' + str_T(M[i-1]) + ' * ' + str_T(M[i]) + ']'

	return R


def str_T(tup): 
    res = 'x'.join(map(str, tup))
    return res


M = [(10,30), (30,5), (5,60)]
M = [(10,30), (30,5), (5,60), (60,1), (1, 10), (10, 4)]
n = len(M)

D, B = mtx_mult(M)
expr = show(M, B, n-1, n)


print(D)
print()

print(B)
print()

print(expr)