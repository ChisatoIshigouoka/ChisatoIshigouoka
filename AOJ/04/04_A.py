d = lambda x, y:x // y
r = lambda x, y:x % y
a,b = map(int,input().split())
g = lambda x, y:x / y
print(f"{d(a,b)} {r(a,b)} {g(a,b):.6f}")