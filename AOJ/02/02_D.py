W, H, x, y, r = map(int, input().split())
if 2 * r <= W and 2 * r <= H and W - x >= r and H - y >= r and x > 0 and y > 0:
    print("Yes")
else:
    print("No")
