

# TODO: Messy Implementation

# https://www.geeksforgeeks.org/maximum-absolute-difference-between-sum-of-two-contiguous-sub-arrays/
#

def pos(b):
	if b:
		return lambda x,y: x >= y
	else:
		return lambda x,y: x <= y


def dynamic(L, n, ineq, oper):
	I    = [0 for i in range(n)]
	F    = [0 for i in range(n)]
	
	l = 0
	while not ineq(L[l], 0):
	  l += 1
	
	F[l]  = L[l]
	I[l]  = 1
	start = l

	for i in range(start+1,n):
		s_i = sum(L[start:i+1])
		r_i = oper(s_i, F[i-1])

		if ineq(L[i], r_i):
			I[i]   = 1
			F[i]   = L[i]
			start  = i
		else:
			F[i] = r_i
			if ineq(s_i, F[i-1]):
				l = i
				while l >= start:
					if I[l] == 1:
						break
					I[l] = 1
					l -= 1
	return F, I


def solve(L,n):
	# Prepare the Dynamic Programming
	#
	RL = list(reversed(L))
	
	Fmax, Imax = dynamic(L,  n, pos(True),  max)
	Fmin, Imin = dynamic(L,  n, pos(False), min)
	
	Bmax, Jmax = dynamic(RL, n, pos(True),  max)
	Bmin, Jmin = dynamic(RL, n, pos(False), max)

	Bmax = list(reversed(Bmax))
	Bmin = list(reversed(Bmin))
	Jmax = list(reversed(Jmax))
	Jmin = list(reversed(Jmin))
	
	# Run combineds DP
	res  = 0
	X, Y = [], []
	
	for i in range(n-1):
		curr = max( Fmax[i] - Bmin[i+1],
			 	   -Fmin[i] + Bmax[i+1] )

		if res < curr:
			res = curr
		
			# Swap Variable Names
			A, B = [], []			
			if Fmax[i] - Bmin[i+1] > -Fmin[i] + Bmax[i+1]:
				A, B = Imax, Jmin
			else:
				A, B = Imin, Jmax

			# Store optimal solution
			X, Y = [], []
		
			l = i
			while l >= 0 and A[l] == 1:
				X.insert(0,l)
				l -= 1

			l = i+1
			while l <= n-1 and B[l] == 1:
				Y.append(l)
				l += 1
			
	return res, X, Y


def test():
	Q = [-2, -3, 4, -1, -2, 1, 5, -3]
	Q = [2, -1, -2, 1, -4, 2, 8]
	Q = [-13, 3, -25, 20, -3, 16, 23, 12, -5, -22, -15, 4, -7] 
	n = len(Q)
	
	r, L, R = solve(Q,n)

	print(Q)
	print(r, [Q[i] for i in L], [Q[i] for i in R])
	

test()



