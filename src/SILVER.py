import math

while True:
	try:
		num = int(raw_input())
		if num == 1:
			print 0
		else:
			print int(math.floor(math.log(num,2)))
	except:
		break