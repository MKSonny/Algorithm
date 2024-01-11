import copy
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
l = []

maxx = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    l.append(tmp)
    # if maxx < max(tmp):
    #     maxx = max(tmp)

dQ = deque()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

total = []
total.append(1)
max_cnt = 0

for rain in range(1, 100 + 1):
    cnt = 0
    dis = copy.deepcopy(l)
    for y in range(n):
        for x in range(n):
            if dis[y][x] > rain:
                dQ.append((y, x))
                while dQ:
                    now = dQ.popleft()
                    for i in range(4):
                        ny = now[0] + dy[i]
                        nx = now[1] + dx[i]
                        if 0 <= ny < n and 0 <= nx < n and dis[ny][nx] > rain:
                            dQ.append((ny, nx))
                            dis[ny][nx] = 1
                cnt += 1
    total.append(cnt)

print(max(total))