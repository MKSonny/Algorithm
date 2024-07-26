from collections import deque

def solution(queue1, queue2):
    answer = -2

    d1 = deque(queue1)
    d2 = deque(queue2)

    sum_d1 = sum(queue1)
    sum_d2 = sum(queue2)

    if (sum_d1 + sum_d2) % 2 != 0:
        return -1

    cnt = 0
    flag = False

    n1 = len(d1)
    n2 = len(d2)

    while sum_d1 != sum_d2:
        if cnt >= ((n1 - 1) + (n2 - 1)) * 2:
            return -1
        if len(d1) == 0 or len(d2) == 0:
            flag = True
            break
        if sum_d1 > sum_d2:
            t = d1.popleft()
            d2.append(t)
            sum_d2 += t
            sum_d1 -= t
        else:
            t = d2.popleft()
            d1.append(t)
            sum_d2 -= t
            sum_d1 += t
        cnt += 1

    if flag:
        return -1
    else:
        return cnt