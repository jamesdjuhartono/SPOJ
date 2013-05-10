ans = [0]
for i in xrange(1,101):
	ans.append(ans[i-1] + i**2)

query = int(raw_input())
while query != 0:
	print ans[query]
	query = int(raw_input())