

def TowerOfHanoi(n, src, aux, dest):
	if n == 1:
		print("Elem. " + str(n) + ", Src: " + src + ", Dest: " +  dest)
		return

	TowerOfHanoi(n-1, src, dest, aux)
	print("Elem. " + str(n) + ", Src: " + src + ", Dest: " +  dest)
	TowerOfHanoi(n-1, aux, src, dest)

TowerOfHanoi(4, 'A', 'B', 'C')
