import sys

s = sys.stdin.readline().rstrip()

l = [0 for _ in range(ord('Z') - ord('A') + 1)]

for i in s:
    t = ord(str.upper(i)) - ord('A')
    l[t] += 1

maxx = -1
max_char = 0


for i in range(ord('Z') - ord('A') + 1):
    if l[i] > maxx:
        maxx = l[i]
        max_char = i

cnt = 0

for i in range(ord('Z') - ord('A') + 1):
    if l[i] == maxx:
        cnt += 1

if cnt >= 2:
    print('?')
else:
    print(chr(max_char + ord('A')))