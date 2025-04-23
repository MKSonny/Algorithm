import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

temp = [0] * n

for idx, i in enumerate(li):
    cnt = -1
    st = 0

    while st < n:
        if temp[st] == 0:
            cnt += 1
            if cnt == i:
                temp[st] = idx + 1
                break
        st += 1

for i in temp: print(i, end=' ')