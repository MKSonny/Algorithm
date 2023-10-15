'''
3. 억지기법과 완전 탐색
    1. 선택 정렬
    2. 순차 탐색
    3. 문자열 매칭
    4. 최근접 쌍의 거리
    5. 완전 탐색
    6. 그래프 탐색 (DFS, BFS)
'''

graph = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]

import queue

# left, right, up, down
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    q = queue.Queue()
    q.put((x, y))
    while not q.empty():
        x, y = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.put((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))
'''
4. 축소 정복 기법 -> 모든 경우의 수(상향식, 하향식)
    1. 삽입 정렬
    2. 위상 정렬
    3. 이진 탐색
    4. 거듭제곱 문제
    5. k번째 작은 수 찾기
5. 분할 정복 기법
    1. 병합 정렬
    2. 퀵 정렬
'''
