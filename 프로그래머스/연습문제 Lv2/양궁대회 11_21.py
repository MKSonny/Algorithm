def solution(n, info):
    answer = []
    temp = []

    for i in info:
        temp.append(i + 1)

    pick = []
    for i in range(len(info)):
        if info[i] > 0:
            pick.append(10 - i)

    total = sum(info)

    maxx = 0

    def dfs(li, t, prev, arrows):
        nonlocal total
        nonlocal maxx
        nonlocal answer
        if t == total:
            print('li', li, sum(li))
            if maxx <= sum(li):
                p_total = 0
                for i in pick:
                    if i not in li:
                        p_total += i
                if sum(li) > p_total:
                    maxx = sum(li)
                    answer.append((li[:], arrows[:]))
                    # answer.append(arrows[:])
            return
        for i in range(prev, len(temp)):
            t += temp[i]
            li.append(10 - i)
            arrows.append(temp[i])
            dfs(li, t, i + 1, arrows)
            arrows.pop()
            li.pop()
            t -= temp[i]

    dfs([], 0, 0, [])
    final_list = []

    # print(answer)

    for i in answer:
        if sum(i[0]) < maxx:
            answer.remove(i)

    if len(answer) == 0:
        return [-1]

    for i in answer:
        temp_final = [0 for _ in range(len(info))]
        for j, a in zip(i[0], i[1]):
            temp_final[10 - j] = a
        final_list.append(temp_final)

    for i in final_list:
        print(i)
    if len(final_list) == 1:
        return final_list.pop()
    else:
        for i in final_list:
            print(i)
    return answer