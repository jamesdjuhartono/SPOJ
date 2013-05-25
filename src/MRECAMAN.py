a = [0]
memo = {}
memo[0] = 1
for x in xrange(1,500001):
	test = a[x-1] - x
	if test > 0 and test not in memo:
		memo[test] = 1
		a.append(test)
	else:
		memo[test + 2*x] = 1
		a.append(test + 2*x)

k = int(raw_input())
while k != -1:
	print a[k]
	k = int(raw_input())