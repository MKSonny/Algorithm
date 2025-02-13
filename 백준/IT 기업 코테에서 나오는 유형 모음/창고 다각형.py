import heapq
import sys

n = int(sys.stdin.readline())
graph = [0 for _ in range(1001)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x] = y


a = graph.index(max(graph))
answer = 0
maxx = 0
for i in range(a + 1):
    maxx = max(maxx, graph[i])
    answer += maxx
# print(answer)
maxx = 0
for j in range(1000, a, -1):
    maxx = max(maxx, graph[j])
    answer += maxx
print(answer)