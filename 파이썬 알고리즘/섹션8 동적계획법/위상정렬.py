n, m = map(int, input().split())

l = [[] for _ in range(n)]
'''
6 6
1 4
5 4
4 3
2 5
2 3
6 2
'''

res = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    l[a - 1].append(b - 1)
    res[b - 1] += 1

# print(l)
# print(res)
q = []
visited = [False] * n

for i in range(n):
    if res[i] == 0 and not visited[i]:
        q.append(i)
        visited[i] = True

while q:

    val = q.pop(0)

    print(val + 1, end=' ')
    for j in l[val]:
        res[j] -= 1

    for i in range(n):
        if res[i] == 0 and not visited[i]:
            q.append(i)
            visited[i] = True