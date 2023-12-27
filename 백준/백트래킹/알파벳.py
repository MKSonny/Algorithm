import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(input().strip()))

mark = [[0 for _ in range(m)] for _ in range(n)]

def isSafe(l, y, x, sol, mark):
    if x >= 0 and x < m and y >= 0 and y < n:
        if l[y][x] not in sol and mark[y][x] == 0:
            return True
    return False

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

max_len = 0

def move(l, y, x, sol, mark):
    global max_len

    if not isSafe(l, y, x, sol, mark):
        return False

    sol.append(l[y][x])
    print(sol)
    # mark[y][x] = 1

    if max_len < len(sol):
        max_len = len(sol)


    if move(l, y, x + 1, sol, mark):
        return True
    if move(l, y, x - 1, sol, mark):
        return True
    if move(l, y - 1, x, sol, mark):
        return True
    if move(l, y + 1, x, sol, mark):
        return True

    sol.pop()

move(l, 0, 0, [], mark)
print(max_len)