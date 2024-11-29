def solution(relation):
    answer_list = list()

    for i in range(1, 1 << len(relation[0])):
        tmp_sets = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += relation[j][k]
            tmp_sets.add(tmp)

        # 만약 len(temp_set)이 len(relation) 보다 작다면 같은 중복되는 값이 있다는 것
        if len(tmp_sets) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)

    return len(answer_list)