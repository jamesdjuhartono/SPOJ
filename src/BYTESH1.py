t = [1, 2]
u = [0, 1]
l = [0, 1]

tc = int(raw_input())
for i in xrange(tc):
    n = int(raw_input())
    if n > len(t):
        for x in xrange(len(t), n):
            t.append((t[x-1] + t[x-2] + u[x-1] + l[x-1]) % 10000)
            u.append((l[x-1] + t[x-2]) % 10000)
            l.append((u[x-1] + t[x-2]) % 10000)
    print t[n-1]
