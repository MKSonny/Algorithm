from collections import deque


def solution(order):
    answer = 1

    l = deque([i for i in range(1, len(order) + 1)])
    # [1, 2, 3, 4, 5]
    temp = deque([])

    idx = 0
    o = order[idx]

    while l:
        i = l.popleft()
        if i == o:
            idx += 1
            break
        temp.append(i)

    # print(order[idx])
    print(temp, l)

    while idx < len(order):
        # if temp and order[idx] == temp[0]:
        #     temp.popleft()
        #     idx += 1
        #     continue
        if temp and order[idx] == temp[-1]:
            temp.pop()
            idx += 1
            answer += 1
            continue
        # if l and order[idx] == l[-1]:
        #     l.pop()
        #     idx += 1
        #     answer += 1
        #     continue
        if l and order[idx] == l[0]:
            l.popleft()
            idx += 1
            answer += 1
            continue
        break

    # print(temp, l)

    return answer