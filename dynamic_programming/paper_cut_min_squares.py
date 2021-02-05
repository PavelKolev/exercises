

# https://www.geeksforgeeks.org/paper-cut-minimum-number-squares-set-2/
#

# Assuming m <= n
#
def solve(m,n):
	T = [[0 for y in range(n+1)] for x in range(m+1)]

	# Initialize
	#
	for i in range(1,m+1):
		T[i][1] = i

	for j in range(1,n+1):
		T[1][j] = j

	for l in range(2,m+1):
		T[l][l] = 1

	# Main Part
	#
	for i in range(2,m+1):
		for j in range(i+1,n+1):
			
			# Horizontal
			V = min( [T[i][j-h] + T[i][h] for h in range(1, 1 + j//2)] )

			# Vertical
			H = min( [T[i-v][j] + T[v][j] for v in range(1, 1 + i//2)] )

			T[i][j] = min(V,H)
			
			if j <= m:
				T[j][i] = min(V,H)

	return T


def test():
	m = 5
	n = 6
	T = solve(m,n)

	for i in range(m+1):
		s = ''
		for j in range(n+1):
			s += '{:2d}'.format(T[i][j]) + ' '
		print(s)


test()