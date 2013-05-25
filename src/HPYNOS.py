def breaknum(n):
	res = 0
	while n:
		res += (n % 10)**2
		n /= 10
	return res

memo = {}
while True:
	try:
		n = int(raw_input())
	except:
		break

	if n in memo:
		print memo[n]
		continue

	ls = [n]
	res = breaknum(n)
	while res not in ls:
		ls.append(res)
		res = breaknum(res)

	if ls[-1] == 1:
		for idx, num in enumerate (ls):
			memo[num] = len(ls) - idx - 1
		print len(ls)-1
	else:
		for num in ls:
			memo[num] = -1
		print -1