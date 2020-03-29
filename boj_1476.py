import sys

li = list(map(int, sys.stdin.readline().split()))
E, S, M = li[0], li[1], li[2]

result = 1

while 1:
    if ((result-E)%15 == 0) and ((result-S)%28 == 0) and ((result-M)%19 == 0):
        print(result)
        break
    else:
        result += 1

