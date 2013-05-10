while True:
	try:
		num = raw_input()
		if num[-1] == '0':
			print 2
		else:
			print 1
			print num[-1]
	except:
		break