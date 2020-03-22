import sys

# Euclidean algorithm
def div(a, b):
    while b > 0:
        b, a = a%b, b
    return a

def mul(a, b):
    m = div(a, b)
    result = a*b//m
    return result

ipt = list(map(int, sys.stdin.readline().split()))
if ipt[0] > ipt[1]:
    ipt[0], ipt[1] = ipt[1], ipt[0]

print(div(ipt[0], ipt[1]))
print(mul(ipt[0], ipt[1]))
