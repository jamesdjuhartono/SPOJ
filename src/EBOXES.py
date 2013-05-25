tc = int(raw_input())

for i in xrange(tc):
	n, k, t, f = map(int, raw_input().split())
	print f + (f-n)/(k-1)