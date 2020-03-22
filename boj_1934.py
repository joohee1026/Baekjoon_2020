import sys

def GCD(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def LCM(a, b):
    return (a*b)//GCD(a, b)

num = int(sys.stdin.readline())

for i in range(0, num):
    ipt = list((map(int, sys.stdin.readline().split())))
    ipt.sort()
    print(LCM(ipt[0], ipt[1]))