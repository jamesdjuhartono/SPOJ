tc = int(raw_input())

for i in xrange(tc):
	n, m = map(int, raw_input().split())
	
	pq = map(int, raw_input().split())
	key = [j for j in xrange(n)]
	normalq = zip(pq,key)
	pq = sorted(pq, reverse = True)
	
	time = 0
	while normalq:
		priority, index = normalq[0]
		del normalq[0]
		if priority == pq[0]:
			time += 1
			del pq[0]
			if index == m:
				break
		else:
			normalq.append((priority, index))

	print time