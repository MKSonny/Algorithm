import sys
sys.setrecursionlimit(100000)

n, m = map(int, sys.stdin.readline().split())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited = [[False for _ in range(m)] for _ in range(n)]

max_cnt = 0

'''
6 5
1 1 0 1 1
0 1 1 0 0
0 0 1 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
'''

def dfs(y, x):
    global cnt
    if 0 <= y < n and 0 <= x < m:
        if board[y][x] == 1 and not visited[y][x]:
            cnt += 1
            board[y][x] = cnt
            visited[y][x] = True
            # max_cnt = max(max_cnt, cnt)
            dfs(y - 1, x)
            dfs(y + 1, x)
            dfs(y, x - 1)
            dfs(y, x + 1)
    else: return

total = 0

max_cnt = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            max_cnt = max(max_cnt, cnt)
            total += 1

# for i in board:
#     print(i)

print(total)
if total == 0: print(0)
else: print(max_cnt)