import random, sys

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
	
    for repeat in xrange(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def paths(graph, start, end):

    todo = [(start,0)]
    while len(todo):
        curr_node, depth = todo.pop(0)
        if curr_node == end:
            return depth
        else:
            for next_node in graph[curr_node]:
                todo.append((next_node, depth+1))
    return -1

primes = []
for i in xrange(1000, 10000):
    if miller_rabin(i):
        primes.append(i)

graph = {}
for i in primes:
    adj = []
    digits = [(i/1000)%10, (i/100)%10, (i/10)%10, i%10]
    for x in xrange(4):
        num = i - digits[x] * 10**(3-x)
        for y in xrange(10):
            if x == 0 and y == 0:
                continue
            newnum = num + y * 10**(3-x)
            if newnum in primes and newnum != i:
                adj.append(newnum)
    graph[i] = adj

print paths(graph,1033,8179)
