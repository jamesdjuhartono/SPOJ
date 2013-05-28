# too slow. use c++ version
tc = int(raw_input())
for case in xrange(tc):
    n = int(raw_input())
    towns = []
    for i in xrange(n):
        towns.append(map(int, raw_input().split()))

    for i in xrange(n):
        for j in xrange(i+1, n):
            currdist = towns[i][j]
            neighbour = True
            for k in xrange(n):
                if k == i or k == j:
                    continue
                elif towns[i][k] + towns[k][j] == currdist:
                    neighbour = False
                    break
            if neighbour is True:
                print i+1, " ", j+1

    if case != tc-1:
        raw_input()
        print ""
