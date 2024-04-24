def solution(cards1, cards2, goal):
    answer = ''
    idx_1 = 0
    idx_2 = 0
    n1 = len(cards1)
    n2 = len(cards2)

    while goal:
        g = goal[0]

        if idx_1 < n1 and cards1[idx_1] == g:
            idx_1 += 1
            goal.pop(0)
        elif idx_2 < n2 and cards2[idx_2] == g:
            idx_2 += 1
            goal.pop(0)
        else:
            return "No"

    return "Yes"