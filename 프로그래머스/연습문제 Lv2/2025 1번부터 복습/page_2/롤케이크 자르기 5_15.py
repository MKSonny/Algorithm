from collections import deque


def solution(topping):
    answer = 0
    t = topping

    right = deque(t)
    right_set = {}

    for i in right:
        if i not in right_set.keys():
            right_set[i] = 1
        else:
            right_set[i] += 1

    left = []
    left_set = {}

    while right:
        a = right.popleft()
        right_set[a] -= 1

        if right_set[a] == 0:
            del (right_set[a])

        left.append(a)

        if a not in left_set.keys():
            left_set[a] = 1
        else:
            left_set[a] += 1

        if len(right_set) == len(left_set):
            answer += 1

    return answer