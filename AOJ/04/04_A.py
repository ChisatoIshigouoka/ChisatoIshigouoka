def d(x, y):
    return x // y


def r(x, y):
    return x % y


def g(x, y):
    return x / y


a, b = map(int, input().split())
print(f"{d(a,b)} {r(a,b)} {g(a,b):.6f}")
