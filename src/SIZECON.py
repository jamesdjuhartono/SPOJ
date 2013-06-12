t = input()
print sum(n for n in (input() for x in range(t)) if n > 0)
