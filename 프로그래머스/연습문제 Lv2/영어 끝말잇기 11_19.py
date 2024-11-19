def solution(n, words):
    answer = []

    temp = []

    for j in range(len(words) - 1):
        if words[j][-1] != words[j + 1][0] or words[j + 1] in temp:
            w = j
            return [(j + 1) % n + 1, (j + 1) // n + 1]
        else:
            temp.append(words[j])
    return [0, 0]

    # if w == -1:
    #     return [0, 0]
    # else:
    #     w += 1
    #     for i in range(len(l)):
    #         for j in range(len(l[i])):
    #             if l[i][j] == words[w]:
    #                 return [i + 1, j + 1]

    return answer