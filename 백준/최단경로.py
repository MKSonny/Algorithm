import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())

h = []
INF = float("inf")
dist = [INF] * (n + 1)
dist[start] = 0
node = [[] for _ in range(n + 1)]


for _ in range(m):
    v1, v2, w = map(int, input().split())
    node[v1].append((v2, w))


# print(dist)

heapq.heappush(h, (0, start))

while len(h) != 0:
    w, start_point = heapq.heappop(h)
    # v1은 출발지
    # k[0]는 목적지
    # print(w, start_point)
    # if dist[v1]
    if w > dist[start_point]:
        continue
    for k in node[start_point]:
        # print(k)
        # 2 + 5 < 3
        # print('dist[%d]' %v1, dist[v1])
        if w + k[1] < dist[k[0]]:
            dist[k[0]] = w + k[1]
            # print(dist)
            heapq.heappush(h, (dist[k[0]], k[0]))

for i in range(1, n + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
# print(dist)