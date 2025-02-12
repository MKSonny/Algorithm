import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

ladders = {}
snakes = {}

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ladders[a] = b

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    snakes[a] = b

visited = [False] * 101
q = deque([1])

flag = True
cnt = 0

while flag:

    length = len(q)

    for _ in range(length):
        x = q.popleft()

        if x == 100:
            flag = False
            print(cnt)
            exit()

        for i in range(1, 7):
            nx = x + i
            if 0 <= nx < 101 and not visited[nx]:
                if nx in ladders.keys():
                    q.append(ladders[nx])
                    visited[ladders[nx]] = True
                elif nx in snakes.keys():
                    q.append(snakes[nx])
                    visited[snakes[nx]] = True
                else:
                    q.append(nx)
                    visited[nx] = True
    # print(q)
    cnt += 1