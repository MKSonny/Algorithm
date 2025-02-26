import sys

n = int(sys.stdin.readline())
answer = 0

loc = []

for i in range(n):
    loc.append(int(sys.stdin.readline().split()[1]))
loc.append(0)

s = [0]

for p in loc:
    height = p
    while s[-1] > p:
        if s[-1] != height:
            answer += 1
            height = s[-1]
        s.pop()
    s.append(p)

print(answer)