import sys
MAX = 1000001
num = 1

li = [True] * MAX
li[0], li[1] = False, False

prime_num = []

for i in range(2, MAX):
    if li[i] == False:
        continue
    elif li[i]:
        prime_num.append(i)
        for j in range(i + i, MAX, i):
            li[j] = False

while 1:
    num = int(sys.stdin.readline())
    if num == 0: break

    brk = False

    for i in range(0, len(prime_num)):
        if li[num - prime_num[i]]:
            print(num, '=', prime_num[i], '+', num - prime_num[i])
            break

'''
    for i in range(num-1, 0, -1):
        for j in range(0, i):
            if prime_num[i] == num - prime_num[j]:
                print(num, '=', prime_num[j], '+', prime_num[i])
                brk = True
                break
        if brk: break
    if brk == False: print("Goldbach's conjecture is wrong.")
'''