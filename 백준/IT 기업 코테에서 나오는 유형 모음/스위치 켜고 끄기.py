import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
std_cnt = int(sys.stdin.readline())

def switch_on(s, number, l):
    if s == 1:
        for i in range(1, n // number + 1):
            l[i * number  - 1] = int(not l[i * number - 1])
    else:
        number -= 1
        l[number] = int(not l[number])
        for i in range(1, n):
            if number + i > n - 1 or number - i < 0:
                break
            if l[number + i] == l[number - i]:
                # number = 2
                # 0, 4, i = 2
                # print(number + i, number - i)
                l[number + i] = int(not l[number + i])
                l[number - i] = l[number + i]
            else:
                break


for _ in range(std_cnt):
    s, number = map(int, sys.stdin.readline().rstrip().split())
    switch_on(s, number, l)

for i in range(1, len(l) + 1):
    print(l[i - 1], end=' ')
    if i % 20 == 0:
        print()