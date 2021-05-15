def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x / y


def dev(x, y):
    return x * y


while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)
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
