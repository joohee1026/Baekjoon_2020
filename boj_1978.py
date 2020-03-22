import sys
import math

# 정수 N이 있을 때, 2부터 N의 제곱근까지 N을 나누어 나누어 떨어지지 않으면 소수
# 제곱근이 2인 경우는 예외처리

n = sys.stdin.readline()
li = list(map(int, sys.stdin.readline().split()))

if 1 in li:
    li.remove(1)

result = 0

for i in range(0, len(li)):
    a = int(math.sqrt(li[i]))
    if a == 1:
        result += 1
        continue
    elif a == 2 and li[i]%2 == 0:
        continue
    elif a == 2 and li[i]%2 != 0:
        result += 1
        continue
    j = 2
    while j <= a and (li[i] % j) != 0:
        j += 1
    if j == a+1:
        result += 1

print(result)