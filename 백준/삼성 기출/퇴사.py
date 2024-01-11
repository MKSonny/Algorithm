import sys

input = sys.stdin.readline

n = int(input())

l = []

for i in range(n):
    day, val = map(int, input().split())
    l.append((day, val))

# n = 7

def dfs(l, level, total):
    day = l[level][0]
    val = l[level][1]

    if level + day < n:
        total += val
        return dfs(l, level + day, total)
    elif level + day == n:
        total += val
        return total
    else:
        return total

h = []

for i in range(n):
    h.append(dfs(l, i, 0))

print(h)

'''
7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
'''