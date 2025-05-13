def solution(k, tangerine):
    answer = 0

    di = {}

    for i in tangerine:
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1

    temp = []

    for i in di.keys():
        temp.append((i, di[i]))

    temp.sort(key=lambda o: o[1])

    while True:
        a, b = temp.pop()

        k -= b
        answer += 1

        if k <= 0: break

    return answer