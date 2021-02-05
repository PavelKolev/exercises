
# https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
#
# Assumming p is a prime number, so as to apply a^(p-1) == 1 mod p
#


def power(x, n):
	if n == 0:
		return 1
	
	if n % 2 == 0:
		return power(x, n/2) * power(x, n/2)
	
	if n % 2 == 1:
		return x * power(x, n-1)


def mod_power(x, n, p):
	a = n % p
	b = (n - a) / p
	return (m_power(x, a, p) * m_power(x, b, p)) % p


def m_power(x, n, p):
	if n == 0:
		return 1
	
	if n % 2 == 0:
		return (m_power(x, n/2, p) * m_power(x, n/2, p) ) % p
	
	if n % 2 == 1:
		return (x * m_power(x, n-1, p)) % p


def test():
	for i in range(10+1):
		print(power(2, i))

	print()
	for i in range(20+1):
		print(mod_power(2, i, 11))


test()