n = int(input())

l = []

for i in range(n):
    day, val = map(int, input().split())
    l.append((day, val))
#

def dfs(l, level, total):
    if level >= n:
        return total

    day = l[level][0]
    val = l[level][1]

    total += val
    return dfs(l, level + day, total)

h = []

for i in range(n):
    h.append(dfs(l, i, 0))

print(max(h))

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