import math
s = lambda x: r ** 2 * math.pi
l = lambda x: 2 * r * math.pi
r = float(input())
print(f"{s(r):.6f} {l(r):.6f}")
