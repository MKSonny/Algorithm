from collections import deque


def solution(n, wires):
    answer = -1

    def bfs(graph, start):
        visited = set()
        q = deque([start])
        visited.add(start)
        cnt = 1
        while q:
            n = q.popleft()
            for k in graph[n]:
                if k not in visited:
                    q.append(k)
                    visited.add(k)
                    cnt += 1
        return cnt

    node = [[] for _ in range(n + 1)]

    for a, b in wires:
        node[a].append(b)
        node[b].append(a)

    minn = float('inf')

    for a, b in wires:
        node[a].remove(b)
        node[b].remove(a)
        minn = min(minn, abs(bfs(node, a) - bfs(node, b)))
        node[a].append(b)
        node[b].append(a)

    return minn