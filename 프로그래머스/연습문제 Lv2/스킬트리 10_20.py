def solution(skill, skill_trees):
    answer = 0

    di = {}

    idx = 0
    for i in skill:
        di[i] = idx
        idx += 1

    for i in skill_trees:
        flag = False
        prev = -1

        if flag: break

        for k in i:
            if k in di:
                if prev == -1 and di[k] != 0:
                    flag = True
                    break
                if prev != -1 and di[k] - prev > 1:
                    flag = True
                    break

                prev = di[k]

        if flag == False:
            answer += 1

    return answer