def solution(skill, skill_trees):
    answer = 0
    mod = []

    alpha = list(skill)

    di = {}

    for i in range(len(alpha)):
        di[alpha[i]] = i

    for sk in skill_trees:
        temp = []
        for i in sk:
            if i not in alpha:
                continue
            temp.append(di[i])
        mod.append(temp)

    for i in mod:
        start = 0
        flag = True

        for j in i:
            if j != start:
                flag = False
                break
            start += 1

        if flag:
            answer += 1

    return answer