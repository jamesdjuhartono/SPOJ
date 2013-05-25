def josephus_2( n ):
	from math import log
	return 2*(n - 2**(int(log(n,2))))+1

while True:
	inp = raw_input()
	n = (int(inp[0])*10 + int(inp[1])) * 10**int(inp[-1])
	if n == 0:
		break
	print josephus_2(n)