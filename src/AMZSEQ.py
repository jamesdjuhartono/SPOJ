a = b = c = 1

x = int(raw_input()) - 1
while x:
    a, b, c = a + b, a + b + c, b + c
    x -= 1

print a + b + c
