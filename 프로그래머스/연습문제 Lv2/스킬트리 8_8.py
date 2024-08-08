def solution(skill, skill_trees):
    answer = 0

    s = set(skill)
    skill = list(skill)

    d = {}
    idx = 0

    for i in skill:
        d[i] = idx
        idx += 1

    for t in skill_trees:
        t = list(t)
        cur = -1
        flag = True
        for k in t:
            if flag == False:
                break
            if k in s:
                if cur == -1 and k != skill[0]:
                    flag = False
                    break
                if d[k] < cur or d[k] - cur > 1:
                    flag = False
                    break
                else:
                    cur = d[k]
        if flag:
            # print(t)
            answer += 1

    return answer