import sys

n = int(sys.stdin.readline())

l = []
cnt = {}

for _ in range(n):
    number = int(sys.stdin.readline())
    l.append(number)
    if number not in cnt.keys():
        cnt[number] = 1
    else:
        cnt[number] += 1

s = sum(l)

l.sort()
temp = []

max_cnt = max(cnt.values())

for key in cnt.keys():
    if cnt[key] < max_cnt:
        continue
    temp.append(key)

temp.sort()

print(round(s / n))
print(l[n // 2])
if len(temp) > 1:
    print(temp[1])
else:
    print(temp[0])
print(l[-1] - l[0])