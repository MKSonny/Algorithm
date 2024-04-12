import heapq
import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().rstrip().split())))

l.sort()
temp = []

maxx = -1
def look_both_side(l, i):
    global maxx
    if i == 0 or i == (n - 1):
        temp.append(l[i])
        if maxx > l[i][1]:
            print(l[i][1], i)
        maxx = max(l[i][1], maxx)
        return True
    if l[i][1] > l[i - 1][1] and l[i][1] > l[i + 1][1]:
        if maxx > l[i][1]:
            print(l[i][1])
        maxx = max(l[i][1], maxx)
        temp.append(l[i])
        return True
    return False

for i in range(n):
    look_both_side(l, i)

print(temp)