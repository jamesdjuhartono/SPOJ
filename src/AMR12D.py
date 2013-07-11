tc = int(raw_input())
while tc > 0:
    magical = True

    inp = raw_input()
    for i in xrange(len(inp)):
        for j in xrange(i+1, len(inp)+1):
            sub = inp[i:j]
            subrev = sub[::-1]
            if subrev not in inp:
                magical = False
                break
        if not magical:
            break

    if magical is True:
        print "YES"
    else:
        print "NO"

    tc -= 1
