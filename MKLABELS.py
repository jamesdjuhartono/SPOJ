casecounter = 1
while True:
	try:
		num = int(raw_input())
		if num == 0:
			break
		elif num == 1:
			print "Case %d, N = %d, # of different labelings = 1" % (casecounter, num)
			casecounter += 1
		else:
			print "Case %d, N = %d, # of different labelings = %d" % (casecounter, num, num**(num-2))
			casecounter += 1
	except:
		break