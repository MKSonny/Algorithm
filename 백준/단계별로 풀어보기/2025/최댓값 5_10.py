import sys

l = []

for _ in range(9):
    l.append(list(map(int, sys.stdin.readline().split())))

maxx = -1
r = 0
c = 0

for i in range(9):
    for j in range(9):
        if l[i][j] > maxx:
            maxx = l[i][j]
            r = i
            c = j

print(maxx)
print(r + 1, c + 1)