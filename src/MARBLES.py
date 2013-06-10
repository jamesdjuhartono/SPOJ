def choose(n, k):
    if 0 <= k <= n:
        p = 1
        for t in xrange(min(k, n - k)):
            p = (p * (n - t)) // (t + 1)
        return p
    else:
        return 0


tc = int(raw_input())
for i in xrange(tc):
    n, k = map(int, raw_input().split())
    print choose(n-1, k-1)
