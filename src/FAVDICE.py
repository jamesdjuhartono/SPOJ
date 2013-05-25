def expectedVal(n):
	
	val = 0.0
	for i in xrange(1,n+1):
		val += n*1.0/i

	return val

tc = int(raw_input())
for i in xrange(tc):
	num = int(raw_input())
	print ("%.2f" % expectedVal(num))