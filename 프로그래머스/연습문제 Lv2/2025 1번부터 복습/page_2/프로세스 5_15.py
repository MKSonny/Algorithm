from collections import deque


def solution(priorities, location):
    answer = 0

    q = []

    for i in range(len(priorities)):
        q.append((priorities[i], i))

    q = deque(q)

    di = {}

    for i in priorities:
        if i not in di.keys():
            di[i] = 1
        else:
            di[i] += 1

    cnt = 0

    while q:
        a, idx = q.popleft()

        if a != max(di.keys()):
            q.append((a, idx))
        else:
            cnt += 1

            if idx == location:
                return cnt

            di[a] -= 1
            if di[a] == 0:
                del di[a]

    return answer