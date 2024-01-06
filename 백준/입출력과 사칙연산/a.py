n = int(input())
l = list(map(int, input().split()))
m = int(input())

cnt = 0
for i in range(n):
    if l[i] == m:
        cnt += 1

print(cnt)