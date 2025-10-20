def solution(order):
    answer = 0

    sub = []
    turn = 0

    for i in range(1, len(order) + 1):
        sub.append(i)

        while sub:
            if sub[-1] == order[turn]:
                answer += 1
                turn += 1
                sub.pop()
            else:
                break

    return answer