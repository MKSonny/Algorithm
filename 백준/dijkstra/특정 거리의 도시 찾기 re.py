import heapq
import sys

input = sys.stdin.readline

n, m, k, start = map(int, input().split())

node = [[] for _ in range(n + 1)]

for _ in range(m):
    starting, ending = map(int, input().split())
    node[starting].append((ending, 1))

print('node', node)

INF = float("inf")
dist = [INF] * (n + 1)
visited = [False] * (n + 1)

h = []
heapq.heappush(h, (0, start))
while h:
    '''
    여기서 힙큐를 사용한 이유는 이전에 getMinVertex는 반복문이 있어 병목현상이 발생한다.
    기존의 다익스트라 알고리즘의 문제점 중 하나는 알고리즘 반복 단계에서 시작 노드와
    가장 거리가 짧은 최단 거리 노드를 찾아야 하는데, 이 때 매번 선형 탐색을 수행해야 한다. 
    '''
    weight, start2 = heapq.heappop(h)
    visited[start2] = True
    # print('test', start2)
    if weight > dist[start2]:
        continue
    # start2 = 1
    # node[1] = [(2, 1), (3, 1)]
    for key in node[start2]:
        # (2, 1): 2가 node 번호, 1이 weight
        # 아래부터는 dijkstra랑 같다.
        if not visited[key[0]]:
            if key[1] + weight < dist[key[0]]:
                dist[key[0]] = key[1] + weight
                heapq.heappush(h, (dist[key[0]], key[0]))

cnt = 0

# print(dist)

for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)