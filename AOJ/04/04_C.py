add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
dev = lambda x, y: x // y
while True:
    t = input().split()
    a = int(t[0])
    op = t[1]
    b = int(t[2])
    if op == "?":
        break
    elif op == "+":
        print(add(a, b))
    elif op == "-":
        print(sub(a, b))
    elif op == "*":
        print(mul(a, b))
    elif op == "/":
        print(dev(a, b))
