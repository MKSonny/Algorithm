# 한 줄씩 입력 받기
n, m = map(int, input().split())  # 첫 줄에서 두 개의 정수를 공백으로 구분하여 입력 받음

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))  # 각 줄에서 숫자들을 공백으로 구분하여 리스트로 변환
    matrix.append(row)

for i in range(n):
    for j in range(m):
        v = matrix[i][j]
        # 0에 들어갈 수 있는 모든 경우의 수를 구해야 한다.
        if v == 0:
            matrix[i][j] = 1
            for k in range(i + 1, n):
                for l in range(j + 1, m):
                    if v == 0:
                        matrix[i][j] = 1
                        for c in range(k + 1, n):
                            for d in range(l + 1, m):
                                matrix[i][j] = 1
        # 아래는 바이러스가 퍼지는 시나리오
        # 벽을 세운 이후 실행시키면 된다.
        if v == 2:
            u = i
            d = i
            while 0 <= u - 1 < n:
                u -= 1
                if matrix[u][j] == 1:
                    break
                matrix[u][j] = 2
            while 0 <= d + 1 < n:
                d += 1
                if matrix[d][j] == 1:
                    break
                matrix[d][j] = 2
            # while 0 <= j - 1 < m:
            #     j -= 1
            #     if matrix[i][j] == 1:
            #         break
            #     matrix[i][j] = 2
            # while 0 <= j + 1 < m:
            #     j += 1
            #     if matrix[i][j] == 1:
            #         break
                matrix[i][j] = 2
            # # left
            # matrix[i][j - 1]
            # # right
            # matrix[i][j + 1]
            # # up
            # matrix[i - 1][j - 1]
            # # down
            # matrix[i + 1][j]

for row in matrix:
    print(row)