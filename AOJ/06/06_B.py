n = int(input())
l1 = []
for i in range(n):
    a, b = input().split()
    l1.append(f"{str(a)} {int(b)}")
l2 = []
for x in ["S", "H", "C", "D"]:
    for y in range(1, 14):
        l2.append(f"{x} {y}")
for l1_item in l1:
    l2.remove(l1_item)
for l2_item in l2:
    print(l2_item)
