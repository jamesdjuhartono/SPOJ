import re

rgx1 = re.compile('(?=(TTT))')
rgx2 = re.compile('(?=(TTH))')
rgx3 = re.compile('(?=(THT))')
rgx4 = re.compile('(?=(THH))')
rgx5 = re.compile('(?=(HTT))')
rgx6 = re.compile('(?=(HTH))')
rgx7 = re.compile('(?=(HHT))')
rgx8 = re.compile('(?=(HHH))')

tc = int(raw_input())
for i in xrange(tc):
	num = int(raw_input())
	inp = raw_input()
	res1 = len(re.findall(rgx1,inp))
	res2 = len(re.findall(rgx2,inp))
	res3 = len(re.findall(rgx3,inp))
	res4 = len(re.findall(rgx4,inp))
	res5 = len(re.findall(rgx5,inp))
	res6 = len(re.findall(rgx6,inp))
	res7 = len(re.findall(rgx7,inp))
	res8 = len(re.findall(rgx8,inp))

	print "%d %d %d %d %d %d %d %d %d" % (num, res1, res2, res3, res4, res5, res6, res7, res8)