import sys

def GCD(a, b):
    while b > 0:
        a, b = b, a%b
    return a

num = int(sys.stdin.readline())

for i in range(0, num):
    li = list(map(int, sys.stdin.readline().split()))
    li = li[1:]
    li.sort()
    result = 0
    for j in range(0, len(li)-1):
        for k in range(j, len(li)-1):
            result += GCD(li[j], li[k+1])
    print(result)