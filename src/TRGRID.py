tc = int(raw_input())

for i in xrange(tc):
	n, m = map(int, raw_input().split())

	if n <= m:
		if n % 2 == 0:
			print "L"
		else:
			print "R"

	else:
		if m % 2 == 0:
			print "U"
		else:
			print "D"