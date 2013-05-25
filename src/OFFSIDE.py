while True:
	a, d = map(int, raw_input().split())
	if a == 0 and d == 0:
		break

	alist = sorted(map(int, raw_input().split()))
	dlist = sorted(map(int, raw_input().split()))
	if alist[0] < dlist[1]:
		print "Y"
	else:
		print "N"