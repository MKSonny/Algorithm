from collections import deque


def solution(s):
    answer = []

    def change(num):
        temp = deque([])

        while num:
            temp.appendleft(num % 2)
            num //= 2

        return temp

    s = list(map(int, s))

    t_cnt = 0
    cnt = 0

    while True:
        t = []
        t_cnt += 1

        for i in s:
            if i == 0:
                cnt += 1
                continue
            t.append(i)

        s = change(len(t))

        if len(s) == 1: break

    return [t_cnt, cnt]