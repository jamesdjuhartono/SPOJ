tc = int(raw_input())
s = []
revidx = {}

for i in xrange(tc):
    num = int(raw_input())
    s.append(num)
    revidx[num] = i+1

a = []
b = []

for item in sorted(s, reverse=True):
    if sum(a) < sum(b):
        a.append(item)
    else:
        b.append(item)

for item in a:
    print revidx[item]
