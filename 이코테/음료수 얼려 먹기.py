n, m = map(int,input().split())

board = []
for i in range(n):
    tmp = list(map(str,input()))
    board.append(list(map(int, tmp)))
visited = board
print(visited)

cnt = 0

def dfs(graph, l, v):
    global cnt
    if graph[l][v] == 0:
        # 그다음 오른 쪽으로 이동
        dfs(graph, l, v + 1)
        # 아래로 먼저 이동
        dfs(graph, l + 1, v)
    else:
        cnt += 1

dfs(board, 0, 0)
print(cnt)