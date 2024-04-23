from collections import deque


def solution(targets):
    answer = 0
    targets.sort(key=lambda o: o[1])
    targets = deque(targets)

    s, e = targets.popleft()
    prev = e
    cnt = 1

    while targets:
        s, e = targets.popleft()

        if prev <= s:
            cnt += 1
            prev = e

    answer = cnt

    return answer