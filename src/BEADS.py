tc = int(raw_input())
for i in xrange(tc):
	word = raw_input()
	bestval = word
	bestidx = 0
	for j in xrange(1,len(word)):
		curr = word[j:] + word[:j]
		if curr < bestval:
			bestval = curr
			bestidx = j
	print bestidx+1