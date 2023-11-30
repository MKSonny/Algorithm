T = int(input())
for _ in range(T):
    n = int(input())
    m = int(input())

    apart = [[0 for _ in range(m)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m):
            if i == 0:
                apart[i][j] = j + 1
            else:
                apart[i][j] = sum(apart[i - 1][:j + 1])

    print(apart[n][m - 1])