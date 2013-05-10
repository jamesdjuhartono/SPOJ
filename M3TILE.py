f = [1,0]
g = [0,1]

for i in xrange(2,31):
	f.append(f[i-2] + 2*g[i-1])
	g.append(f[i-1] + g[i-2])

n = int(raw_input())
while n != -1:
	print f[n]
	n = int(raw_input())