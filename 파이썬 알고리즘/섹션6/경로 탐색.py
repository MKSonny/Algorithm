n, m = map(int, input().split())
l = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    l[a].append(b)
'''
5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5
'''
visited = [False] * (n + 1)
visited[1] = True
cnt = 0

def dfs(l, start, sol):
    global cnt
    if start == n:
        # print(sol)
        cnt += 1
        return

    for i in l[start]:
        if not visited[i]:
            sol.append(i)
            visited[i] = True
            dfs(l, i, sol)
            visited[i] = False
            sol.pop()

dfs(l, 1, [1])
print(cnt)