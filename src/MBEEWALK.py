ls = [0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 1588356, 8676360, 47977776, 266378112, 1488801600]
tc = int(raw_input())

for x in xrange(tc):
    n = int(raw_input())
    print ls[n-1]
