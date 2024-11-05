from collections import deque


def solution(queue1, queue2):
    answer = 0
    s1 = sum(queue1)
    s2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    maxx = len(queue1) * 2 + len(queue2) * 2

    if (s1 + s2) % 2 != 0:
        return -1

    while s1 != s2 and queue1 and queue2:
        if answer > maxx:
            return -1
        if s1 > s2:
            t = queue1.popleft()
            queue2.append(t)
            s1 -= t
            s2 += t
        else:
            t = queue2.popleft()
            queue1.append(t)
            s1 += t
            s2 -= t
        answer += 1
    if s1 != s2:
        return -1

    return answer