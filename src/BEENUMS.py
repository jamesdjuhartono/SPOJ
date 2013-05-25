# too slow. use c++ version
beehive_nums = []

for i in xrange(10**5):
	beehive_nums.append((i**2 + i)/2)

num = int(raw_input())

while num != -1:
	if num % 6 == 1 and (num-1)/6 in beehive_nums:
		print "Y"
	else:
		print "N"
	num = int(raw_input())