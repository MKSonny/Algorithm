def solution(input_string):
    answer = []
    al = list(set(input_string))
    d = {}
    for i in al:
        d[i] = []
    for idx, i in enumerate(input_string):
        d[i].append(idx)

    for k in d:
        for i in range(len(d[k]) - 1):
            if d[k][i] != d[k][i + 1] - 1:
                answer.append(k)

    answer = list(set(answer))

    if len(answer) == 0:
        return 'N'

    answer.sort()
    answer = ''.join(answer)

    return answer