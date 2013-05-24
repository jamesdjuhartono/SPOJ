tc = int(raw_input())
for i in xrange(tc):
	x, y = map(int, raw_input().split())
	if x == y and x % 2 == 0:
		print x+y
	elif x == y and x % 2 == 1:
		print x+y-1
	elif x != y and x-y == 2 and x % 2 == 0:
		print x+y
	elif x != y and x-y == 2 and x % 2 == 1:
		print x+y-1
	else:
		print "No Number"