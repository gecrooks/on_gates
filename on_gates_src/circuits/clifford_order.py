
from math import log

#Table[2^(n^2+2n+3) Product[4^j-1, {j, n}], {n, 0, 10}]



for n in range(1, 9):
	N = 2**(n**2 + 2*n)
	for j in range(1, n+1):
		N *= 4**j - 1

	# print(n, N, log(N, 2), 2*n*(4*n+1) )

	print(f"{n} & {N} & {log(N, 2):.2f} & {2*n*(2*n+1)} \\\\")
