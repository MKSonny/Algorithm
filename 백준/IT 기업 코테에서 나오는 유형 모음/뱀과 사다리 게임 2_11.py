import sys
from collections import deque
from sys import flags

n, m = map(int, sys.stdin.readline().split())

ladders = {}
snakes = {}

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ladders[a] = b

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    snakes[a] = b

q = deque([1])
visited = [False] * 101
visited[1] = False
cnt = 0

flag = True

while flag:
    length = len(q)
    for _ in range(length):
        x = q.popleft()
        if x == 100:
            print(cnt)
            flag = False
            break

        for i in range(1, 7):
            nx = x + i

            if nx <= 100 and not visited[nx]:
                visited[nx] = True
                if nx in ladders.keys():
                    visited[ladders[nx]] = True
                    q.append(ladders[nx])
                elif nx in snakes.keys():
                    visited[snakes[nx]] = True
                    q.append(snakes[nx])
                else:
                    q.append(nx)


    cnt += 1