import sys
sys.setrecursionlimit(10000)
test_case = int(input())

def dfs(y, x):
    if (0 <= y < N) and (0 <= x < M) and matrix[y][x] == 1:
        # 아래의 반복문에서, dfs 함수가 실행된 후에도 다음 행으로 넘어가는 것을 방지하기 위해,
        # 이미 방문한 위치를 -1로 표시하는 방식을 사용한다.
        # 이렇게 하면 이미 방문한 위치를 표시하고 나서 다음 행으로 넘어갈 때, 중복 방문을 피할 수 있다.
        matrix[y][x] = -1
        # 아래는
        # 위
        dfs(y - 1, x)
        # 아래
        dfs(y + 1, x)
        # 왼쪽
        dfs(y, x - 1)
        # 오른쪽
        dfs(y, x + 1)

for i in range(test_case):
    # M, N 사용 주의
    M, N, K = map(int, input().split())
    matrix = [[0]*(M) for _ in range(N)]
    cnt = 0

    for j in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    # 가로길이(열) M(1 ≤ M ≤ 50)
    # 세로길이(행) N(1 ≤ N ≤ 50)
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1:
                dfs(y, x)
                cnt += 1

    print(cnt)