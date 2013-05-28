while True:
    try:
        n = int(raw_input())
    except:
        break
    if n == 1:
        print 1
    else:
        print 2*n - 2
