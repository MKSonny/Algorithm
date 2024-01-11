n = int(input())

t = []
v = []

for i in range(n):
    day, val = map(int, input().split())
    t.append(day)
    v.append(val)

t.insert(0, 0)
v.insert(0, 0)

#

total = 0

def dfs(level, sum):
    global total

    if level == n + 1:
        if sum > total:
            total = sum
    else:
        if level + t[level] <= n + 1:
            dfs(level + t[level], sum + v[level])
        dfs(level + 1, sum)

dfs(1, 0)
print(total)
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