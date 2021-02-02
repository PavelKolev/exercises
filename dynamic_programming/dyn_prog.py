
# https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
#


# Minimum number of jumps

def solve(L):
	n = len(L)

	# [steps, i_k, v_k]
	ram  = [[0,0]]

	# [i_k + v_k + 1, i_{k+1} + v_{k+1}]
	box  = [[0,0]]
	
	k = 0
	while True:
		i_k   = 0
		v_k   = 0
		r_max = 0
		
		for i in range(box[k][0], box[k][1]+1):
			step = i + L[i]
			if r_max <= step:
				r_max   = step
				i_k     = i
				v_k     = L[i]

		#previous
		i_k_ = ram[k][0]
		i_v_ = ram[k][1]

		box.append([i_k_ + i_v_ + 1, i_k + v_k])
		ram.append([i_k, v_k])

		k += 1

		if r_max >= n-1:
			break


	return box, ram, k

def test():
	L = [1,3,5,8,9,2,6,7,6,8,9,1,1,1,1]
	#L = [1,4,5,2,3,2,1]

	box, ram, steps = solve(L)
	print("Index: ", list(range(len(L))))
	print("Input: ", L)
	print("Box:   ", box)
	print("Ram:   ", ram)
	print("Steps: ", steps)


test()