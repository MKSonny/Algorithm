import sys

n, l = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def pos(now, used):
    for j in range(1, n):
        # 차이가 1보다 크면 False 리턴
        if abs(now[j] - now[j - 1]) > 1:
            return False
        if now[j] < now[j - 1]:
            # 높이가 다른 시점부터 검사 시작
            for k in range(l): # l 만큼 경사로 너비 필요
                # j는 높이가 다른 지점의 시작 위치
                # j쪽의 높이가 더 낮음
                # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우
                if j + k >= n or used[j + k] or now[j] != now[j + k]:
                    return False
                # 높이가 같은 경우 사용 여부 체크
                if now[j] == now[j + k]:
                    used[j + k] = True
        elif now[j] > now[j - 1]:
            for k in range(l):
                if j - k - 1 < 0 or now[j - 1] != now[j - k - 1] or used[j - k - 1]:
                    return False
                if now[j - 1] == now[j - k - 1]:
                    used[j - k - 1] = True
    return True

spin = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        spin[n - j - 1][i] = graph[i][j]

answer = 0

for i, j in zip(graph, spin):
    used = [False] * n
    used_spin = [False] * n
    answer += pos(i, used)
    answer += pos(j, used_spin)

print(answer)