import sys
sys.setrecursionlimit(10000)

test_case = int(input())
"""
    아래의 반복문에서, dfs 함수가 실행된 후에도 다음 행으로 넘어가는 것을 방지하기 위해,
    이미 방문한 위치를 -1로 표시하는 방식을 사용한다.
     이렇게 하면 이미 방문한 위치를 표시하고 나서 다음 행으로 넘어갈 때, 중복 방문을 피할 수 있다.
        
    위, 아래, 왼쪽, 오른쪽 4방향 중 인접한 인덱스에 1이 있다면 계속해서
    dfs가 재귀적으로 호출된다. 1이 연속해서 존재하는 모든 탐색을 완료하면
    dfs가 더 이상 호출되지 않아 이전 dfs가 처음 호출되었던 부분부터 다시 코드를 실행하게 된다.
    따라서 아래 cnt += 1이 실행되고 x가 증가하여 다음 인덱스로 넘어간다.
    dfs 함수 내부에 cnt를 추가하는 것이 아니라 즉, dfs가 호출되는 횟수를 세는 것이 아닌
    여기서 dfs 함수의 역할은 1이 존재하는 4곳을 모두 탐색하고 이어져 있는 1들을 모두 -1로 바꾼다.
"""
def dfs(y, x):
    if (0 <= y < N) and (0 <= x < M) and matrix[y][x] == 1:

        matrix[y][x] = -1


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