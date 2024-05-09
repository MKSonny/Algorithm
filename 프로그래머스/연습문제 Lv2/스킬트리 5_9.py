def solution(skill, skill_trees):
    answer = 0

    skill_set = set(skill)

    for i in skill_trees:
        test = list(skill)
        temp = True
        for j in i:
            # print(test, i)
            if j in skill_set:
                if test.pop(0) != j:
                    temp = False
                    break
        if temp:
            answer += 1

    return answer