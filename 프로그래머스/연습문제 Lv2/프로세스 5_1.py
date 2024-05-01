from collections import deque


def solution(priorities, location):
    answer = 0
    l = deque()

    for idx, i in enumerate(priorities):
        l.append((i, idx))

    cnt = 0

    while l:
        a = l.popleft()
        flag = True
        for i in l:
            if i[0] > a[0]:
                l.append(a)
                flag = False
                break
        if flag:
            cnt += 1
            if a[1] == location:
                return cnt

    return answer