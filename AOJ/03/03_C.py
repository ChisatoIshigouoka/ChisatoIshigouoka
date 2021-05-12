t = 0
while True:
    x, y = map(int, input().split())
    t += 1
    if x == 0 and y == 0:
        break
    if x > y:
        print(y, x)
    else:
        print(x, y)
    