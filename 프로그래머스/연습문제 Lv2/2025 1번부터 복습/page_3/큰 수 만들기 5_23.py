from collections import deque


def solution(number, k):
    answer = ''

    q = []

    for i in number:
        if len(q) == 0:
            q.append(i)
            continue
        while k != 0 and q[-1] < i:
            q.pop()
            k -= 1
            if k == 0 or len(q) == 0:
                break
        q.append(i)

    if k != 0:
        q = number[:-k]

    return ''.join(q)