from collections import deque


def solution(queue1, queue2):
    answer = 0

    t1 = sum(queue1)
    t2 = sum(queue2)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    total = (t1 + t2) // 2

    while True:
        while t1 > total:
            a = queue1.popleft()
            t1 -= a
            queue2.append(a)
            t2 += a
            answer += 1

        while t2 > total:
            b = queue2.popleft()
            t2 -= b
            queue1.append(b)
            t1 += b
            answer += 1

        if t1 == t2 == total:
            break

        if answer > (len(queue1) + len(queue2)) * 2:
            return -1

    return answer