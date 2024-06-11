import copy

cnt = 0
from collections import deque
from collections import Counter


def solution(n, wires):
    answer = -1
    wires = deque(wires)

    #     print(node[4])

    def dfs(n):
        visited[n] = True
        global cnt
        cnt += 1
        # print(n, end=' ')
        for key in node[n]:
            if not visited[key]:
                dfs(key)

    minn = float('inf')

    for k in range(len(wires)):
        node = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        temp = wires.pop()
        # print(wires)

        for i in wires:
            a, b = i
            node[a].append(b)
            node[b].append(a)

        for t in range(1, n + 1):
            if not visited[t]:
                cnt = 0
                dfs(t)
                break
        c = Counter(visited[1:])

        minn = min(abs(c[True] - c[False]), minn)

        wires.appendleft(temp)

    answer = minn

    return answer