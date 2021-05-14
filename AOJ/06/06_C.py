l2 = [[0 for i in range(10)]for j in range(12)]
l2_new = []
n = int(input())
l1 = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    l1.append([a, b, c, d])
for l1_list1 in l1:
    a = l1_list1[0]
    b = l1_list1[1]
    c = l1_list1[2]
    d = l1_list1[3]
    e = l2[(a-1)*3+b-1][c-1]
    e += d
    l2[(a-1)*3+b-1][c-1] = e
for l2_item in l2:
    l2_item.insert(0, "")
    l2_new_item = " ".join(map(str, l2_item))
    l2_new.append(l2_new_item)
l2_new.insert(3, "####################")
l2_new.insert(7, "####################")
l2_new.insert(11, "####################")
for l2_new_item in l2_new:
    print(l2_new_item)
