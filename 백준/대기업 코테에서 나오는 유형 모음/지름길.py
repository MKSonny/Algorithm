import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
node = [[] for _ in range(10000 + 1)]
h = []

# 2 100
# 10 60 40
# 50 90 20

temp = []
for _ in range(n):
    start, end, weight = map(int, sys.stdin.readline().rstrip().split())
    temp.append(start)
    temp.append(end)
    if end > m:
        continue
    else:
        node[start].append((end, weight))
    if end > m:
        print(m, end, abs(m - end))
        node[m].append((end, abs(m - end)))
    else:
        # start = 100 -> 110
        node[end].append((m, m - end))

    if start == 0:
        continue
    node[0].append((start, start))

# 100과 연결되어 있는 건 150이라고 나온다.
# 하지만 100과 110은 연결되어있다.
temp = list(set(temp))
temp.sort()
k = len(temp)

for i in range(k - 1):
    for j in range(i + 1, k):
        node[temp[i]].append((temp[j], temp[j] - temp[i]))

# print('node[100]', node[100])


# 0, start
heapq.heappush(h, (0, 0))
INF = float("inf")
dist = [INF] * (10000 + 1)
dist[m] = m
visited = [False] * (10000 + 1)

while h:
    weight, node_number = heapq.heappop(h)
    visited[node_number] = True
    if weight > dist[node_number]:
        continue
    for key in node[node_number]:
        if not visited[key[0]]:
            if weight + key[1] < dist[key[0]]:
                dist[key[0]] = weight + key[1]
                heapq.heappush(h, (dist[key[0]], key[0]))

print(dist[m])
# 문제: 100 ~ 110까지의 정보 없음
# print(node[100])
# for i in range(len(dist)):
#     if dist[i] != INF:
#         print(i, dist[i])