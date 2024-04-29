def solution(m, n, puddles):
    answer = 0

    l = [[0 for _ in range(m)] for _ in range(n)]

    for p in puddles:
        l[p[1] - 1][p[0] - 1] = 'p'

    l[0][0] = 1
    # l[n - 1][m - 1] = 's'

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if l[i][j] == 'p':
                continue
            up = 1
            left = 1

            if i - 1 >= n or i - 1 < 0:
                up = 0
            if j - 1 >= m or j - 1 < 0:
                left = 0
            if l[i - 1][j] == 'p':
                up = 0
            if l[i][j - 1] == 'p':
                left = 0
            l[i][j] = l[i - up][j] + l[i][j - left]

    # for i in l:
    #     print(i)

    answer = l[n - 1][m - 1] % 1000000007

    return answer