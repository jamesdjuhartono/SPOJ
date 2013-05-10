tc = int(raw_input())
for i in xrange(tc):
	n, p = map(int, raw_input().split())
	if p == 0:
		print "Airborne wins."
	else:
		print "Pagfloyd wins."