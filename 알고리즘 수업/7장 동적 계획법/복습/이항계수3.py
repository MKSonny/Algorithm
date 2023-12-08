def coef(n, k):
    table = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                table[i][j] = 1
            # else문이 없을 경우 아래가 무조건 실행되서
            # i = 0, j = 0 일 떄
            # 이전 if문에서 table[0][0]을 1을 적어도
            # 여기서
            # table[0][0] = table[-1][-1] + table[-1][0]
            # table[0][0] = 0 + 0
            # 으로 값이 초기화되어 답이 안나온다.
            table[i][j] = table[i - 1][j - 1] + table[i - 1][j]

    print(table[-1][-1])
    return table[n][k]

print(coef(4, 2))
