import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

cnt = 0

if l[n - 1] == m:
    cnt += 1

for i in range(n - 1):
    summ = l[i]
    if summ > m:
        continue
    elif summ == m:
        cnt += 1
        continue
    for j in range(i + 1, n):
        summ += l[j]
        if summ > m:
            break
        elif summ == m:
            cnt += 1
            break

print(cnt)