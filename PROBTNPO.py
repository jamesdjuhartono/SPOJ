import sys, os
# too slow for SPOJ, use p100 from uVA instead
memo = {}

def f(n):
	count = 1
	while n != 1:
		count += 1
		if n % 2 == 1: #n is odd
			n = 3*n + 1
		else:
			n /= 2
	return count

def solve(n, m):
	ans = 0
	for i in xrange(n, m+1):
		if memo.has_key(i):
			ans = max(ans, memo[i])
		else:
			cycle = f(i)
			memo[i] = cycle
			ans = max(ans, cycle)
	return ans

while 1:
	try:
		line = sys.stdin.readline()
		n = int(line.split()[0])
		m = int(line.split()[1])
		print "%d %d %d" % (n, m, solve(min(n,m), max(n,m)))
	except:
		break