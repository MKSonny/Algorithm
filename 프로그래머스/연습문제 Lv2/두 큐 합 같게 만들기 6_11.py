from collections import deque
import copy


def solution(queue1, queue2):
    answer = 0

    a = sum(queue1)
    b = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    cnt = 0
    n = len(queue1)
    maxx = 3 * n

    '''
    제한은 다음과 같이 queue1의 원소가 queue2로 전부 이동하고, queue2의 원소만 queue1으로 이동하고, 
    남은 queue2의 원소가 queue1으로 이동하는 경우로 len(q1) * 3 이 탐색 제한 범위가 될 수 있다.
    '''

    if a == b:
        return 0
    else:
        while a != b and queue1 and queue2:
            if cnt > maxx:
                return -1
            cnt += 1
            if a < b:
                t = queue2.popleft()
                queue1.append(t)
                a += t
                b -= t
            else:
                t = queue1.popleft()
                queue2.append(t)
                b += t
                a -= t

    # print(cnt)
    if len(queue1) * len(queue2) == 0:
        return -1
    return cnt