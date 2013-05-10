import sys, types

def mcxi_val(mcxi_str):
	res = 0;
	for index, val in enumerate(mcxi_str):
		if val.isdigit() and index+1 < len(mcxi_str):
			ch = mcxi_str[index+1]
			if ch == 'm':
				res += int(val) * 1000;
			elif ch == 'c':
				res += int(val) * 100;
			elif ch == 'x':
				res += int(val) * 10;
			elif ch == 'i':
				res += int(val) * 1;
		elif val.isdigit() == False:
			if (index-1 >= 0 and mcxi_str[index-1].isdigit() == False) or index == 0:
				ch = mcxi_str[index]
				if ch == 'm':
					res += 1000
				elif ch == 'c':
					res += 100
				elif ch == 'x':
					res += 10
				elif ch == 'i':
					res += 1
	#print res
	return res

def mcxi_str(mcxi_val):
	res = ""
	size = len(str(mcxi_val))
	for index, val in reversed(list(enumerate(str(mcxi_val)))):
		ch = ''
		if size - index == 1:
			ch = 'i'
		elif size - index == 2:
			ch = 'x'
		elif size - index == 3:
			ch = 'c'
		elif size - index == 4:
			ch = 'm'

		if val == '0':
			continue
		elif val == '1':
			res = ch + res
		else:
			res = val + ch + res

	return res

tc = int(raw_input())
for i in xrange(tc):
	str1, str2 = raw_input().split(' ')
	sum = mcxi_val(str1) + mcxi_val(str2)
	print mcxi_str(sum)