import sys

li = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 9):
    li[i] = int(sys.stdin.readline().rstrip())

s = sum(li)
del_num = [0, 0]

for i in range(0, 8):
    for j in range(i+1, 9):
        s -= (li[i] + li[j])
        if s == 100:
            del_num[0] = li[i]
            del_num[1] = li[j]
            li.remove(del_num[0])
            li.remove(del_num[1])
            break
        s = sum(li)
    if s == 100: break

li.sort()

for l in li:
    print(l)
