import sys

room = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

cnt = 0
for i in people:
    if i - b > 0:
        i = i - b
        cnt += i // c
        if i % c != 0:
            cnt += 1
    cnt += 1

print(cnt)