import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

decaocton = [0]
for i in xrange(1,66):
	decaocton.append(nCr(i+8, 9))

tc = int(raw_input())
for i in xrange(tc):
	casenum, num = map(int, raw_input().split())
	print "%d %d" % (casenum, decaocton[num+1])
