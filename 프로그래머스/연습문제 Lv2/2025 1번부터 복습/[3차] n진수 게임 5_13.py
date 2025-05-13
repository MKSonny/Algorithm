from collections import deque


def solution(n, t, m, p):
    answer = ''

    maxx = t * m

    di = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def bi(num, t):
        q = deque([])

        while num:
            if num % t >= 10:
                q.appendleft(di[num % t])
            else:
                q.appendleft(num % t)
            num //= t

        return q

    l = [0]

    for i in range(maxx):
        l.extend(bi(i, n))

    for i in range(len(l)):
        if i % m == p - 1:
            answer += str(l[i])

        if len(answer) == t:
            break

    return answer