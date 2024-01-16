n = int(input())

res = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if res[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):
            res[j] += 1

print(cnt)