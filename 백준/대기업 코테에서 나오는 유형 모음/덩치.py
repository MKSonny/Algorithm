import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    weight, height = map(int, sys.stdin.readline().rstrip().split())
    l.append((weight, height))

for my in l:
    rank = 1
    for others in l:
        if my[0] < others[0] and my[1] < others[1]:
            rank += 1
    print(rank, end=' ')