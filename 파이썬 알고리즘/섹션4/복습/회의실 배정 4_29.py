from collections import deque

n = int(input())
l = []
'''
5
1 4
2 3
3 5
4 6 
5 7
'''
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b))

l.sort(key=lambda o:o[1])
prev_s, prev_e = l[0]
cnt = 1

for i in range(1, n):
    s, e = l[i]
    if prev_e <= s:
        prev_e = e
        cnt += 1

print(cnt)