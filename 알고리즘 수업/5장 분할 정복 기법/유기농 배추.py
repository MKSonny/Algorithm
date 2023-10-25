test_case = int(input())

# left, right, down, up
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 행렬만들기
for i in range(T):
    # M, N 사용 주의
    M, N, K = map(int, input().split())
    matrix = [[0]*(M) for _ in range(N)]
    cnt = 0

    for j in range(K):
        x,y = map(int, input().split())
        matrix[x][y] = 1

    for a in range(N):
        for b in range(M):
            if matrix[a][b] == 1:
                dfs(a,b)
                cnt += 1

    print(cnt)