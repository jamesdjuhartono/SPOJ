n = int(raw_input())

bobs = set()
alls = set()

for i in xrange(n):
	data = raw_input().split()
	bobs.add(data[0])
	alls.add(data[0])
	for x in data[2:]:
		alls.add(x)

print len(alls-bobs)