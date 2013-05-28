tc = int(raw_input())

for case in xrange(tc):
    print "Scenario #{c}:".format(c=case+1)

    need, friends = map(int, raw_input().split())
    stamps = sorted(map(int, raw_input().split()), reverse=True)

    if sum(stamps) < need:
        print "impossible"
    else:
        total = 0
        for index, stamp in enumerate(stamps):
            total += stamp
            if total >= need:
                print index+1
                break

    if case != tc-1:
        print ""
