for i in range(10):
    s = raw_input()
    print 2**(sum(s.count(x) for x in 'DLFT'))
