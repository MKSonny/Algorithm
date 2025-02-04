from collections import deque


def solution(n, wires):
    answer = -1

    def bfs(node, visited):
        q = deque([node])
        cnt = 0

        while q:
            a = q.popleft()
            cnt += 1
            visited[a] = True
            for n in l[a]:
                if not visited[n]:
                    q.append(n)
                    # visited[n] = True

        return cnt

    last = wires[-1]
    t = -1

    minn = n + 1

    while t != last:

        l = [[] for _ in range(n + 1)]

        wires = deque(wires)
        t = wires.popleft()

        for a, b in wires:
            l[a].append(b)
            l[b].append(a)

        visited = [False] * (n + 1)

        calc = [0, 0]
        idx = 0

        for i in range(1, n + 1):
            if not visited[i]:
                calc[idx] = bfs(i, visited)
                idx += 1

        wires.append(t)
        minn = min(abs(calc[0] - calc[1]), minn)

    return minn