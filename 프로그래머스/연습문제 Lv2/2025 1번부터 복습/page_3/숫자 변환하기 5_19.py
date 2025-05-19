from collections import deque


def solution(x, y, n):
    answer = 0

    q = deque([(x, 0)])
    v = set()

    while q:
        x, cnt = q.popleft()

        if x in v or x > y:
            continue

        if x == y:
            return cnt

        v.add(x)

        for k in (x + n, x * 2, x * 3):
            q.append((k, cnt + 1))

    return -1