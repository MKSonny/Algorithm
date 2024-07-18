def solution(want, number, discount):
    answer = 0

    d = {}

    for i in range(len(want)):
        d[want[i]] = number[i]

    temp = 10

    n = len(discount)
    temp = discount[:10]

    for i in range(n):
        new_d = {}
        flag = True
        for i in discount[i:i + 10]:
            if new_d.get(i) == None:
                new_d[i] = 1
            else:
                new_d[i] += 1
        for i in d:
            if new_d.get(i) == None:
                flag = False
                break
            elif new_d[i] < d[i]:
                flag = False
                break
        if flag:
            answer += 1

    return answer