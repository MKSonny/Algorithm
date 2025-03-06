import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

l = [[] for _ in range(n)]

for idx in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    for k_idx in range(len(k)):
        if k[k_idx] == 1:
            l[idx].append(k_idx)

# print(l)

target = list(map(int, sys.stdin.readline().split()))

flag = False

def dfs(start, next_idx, visited):

    global flag

    if flag:
        return

    if next_idx == m:
        # print("YES")
        flag = True
        return



    if target[next_idx] - 1 == start:
        visited = [False for _ in range(n)]
        dfs(start, next_idx + 1, visited)
    else:
        for no in l[start]:
            if not visited[no]:
                visited[no] = True
                dfs(no, next_idx, visited)


visited = [False for _ in range(n)]

for i in range(n):
    dfs(i, 0, visited)

if flag:
    print("YES")
else:
    print("NO")
# print(dfs(0, 0, visited))