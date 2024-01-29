n = int(input())

x = 64
l = [64, 32, 16, 8, 4, 2, 1]

cnt = 0
for i in l:
    if n - i < 0:
        continue
    else:
        n -= i
        cnt += 1

print(cnt)