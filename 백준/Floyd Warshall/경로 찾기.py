import sys

input = sys.stdin.readline
n = int(input())
d = []

for _ in range(n):
    d.append(list(map(int, input().split())))

parent = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if d[i][j] == 1:
            parent[i].append(j)


for i in range(n):
    for key in parent[i]:
        print(key)

