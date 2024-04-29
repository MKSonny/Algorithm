def solution(m, n, puddles):
    answer = 0
    print(4 % 1000000007)
    INF = float('inf')
    l = [[INF for _ in range(m)] for _ in range(n)]
    l[0][1], l[1][0] = 1, 1
    l[0][0] = 'h'
    l[n - 1][m - 1] = 's'
    for p in puddles:
        l[p[0] - 1][p[1] - 1] = 'p'

    for i in l:
        print(i)

    print()

    for i in range(n):
        for j in range(m):
            down = 0
            right = 0
            if type(l[i][j]) != str and l[i][j] != 1:
                # print(i, j, type(l[i][j]))
                print(i, j)
                if 0 <= i - 1 < n:
                    down = 1
                if 0 <= j - 1 < m:
                    right = 1
                if type(l[i - down][j]) == str:
                    down = 0
                if type(l[i][j - right]) == str:
                    right = 0
                l[i][j] = min(l[i][j - right], l[i - down][j]) + 1

    for i in l:
        print(i)

    def dfs(l, y, x, visited):
        down, right = 0, 0
        if y < 0 or y >= n or x >= m or x < 0:
            return
        if visited[y][x]:
            return
        visited[y][x] = True
        if 0 <= y - 1 < n:
            down = 1
        if 0 <= x - 1 < m:
            right = 1
        if type(l[y - down][x]) == str:
            down = 0
        if type(l[y][x - right]) == str:
            right = 0
        if l[y][x] == 'u':
            dfs(l, y - 1, x)
        elif l[y - down][x] == l[y][x - right]:
            l[y][x] = 'u'
            dfs(l, y - 1, x, visited)
        else:
            if l[y - down][x] < l[y][x - right]:
                dfs(l, y - 1, x, visited)
            else:
                dfs(l, y, x - 1, visited)

    visited = [[False for _ in range(m)] for _ in range(n)]
    dfs(l, n - 1, m - 1, visited)

    for i in visited:
        print(i)

    for i in l:
        print(i)

    return answer