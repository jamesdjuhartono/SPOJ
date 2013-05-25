#too slow. use cpp version
import sys

data = sys.stdin.read().split('\n')
datalen = len(data)
start = 2

while start < datalen:
	lines = int(data[start-1])
	accts = {}
	for i in xrange(start, start+lines):
		accts[data[i]] = (accts[data[i]] + 1) if data[i] in accts else 1
	keys = accts.keys()
	keys.sort()
	for k in keys:
		sys.stdout.write('%s %i\n' % (k, accts[k]))
	sys.stdout.write('\n')
	start += lines + 2