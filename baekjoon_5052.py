import sys
n = sys.stdin.readline()

for i in range(0, int(n)):
    t = int(sys.stdin.readline().strip())
    num_li = []
    result = 'YES'
    for j in range(0, t):
        num_li.append(sys.stdin.readline().strip())
    num_li.sort()
    for j in range(0, len(num_li)-1):
        if num_li[j] == num_li[j+1][0:len(num_li[j])]:
            result = 'NO'
            break
    print(result)