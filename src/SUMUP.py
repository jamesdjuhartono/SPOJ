t = [x*1.0/(x**4+x**2+1) for x in range(1, 10001)]
a = [0]
for i in range(1,10001): a.append(t[i-1] + a[i-1])
c = int(raw_input())
while c:
    print "%.5f" % a[int(raw_input())]
    c -= 1
#scoring is based on code length, hence the formatting