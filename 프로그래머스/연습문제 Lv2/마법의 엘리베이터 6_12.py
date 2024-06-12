def solution(storey):
    answer = 0
    while storey != 0:
        # 2550
        t = 10 - (storey % 10)
        if storey % 10 > 5:
            storey += t
            answer += t
        elif storey % 10 < 5:
            answer += (storey % 10)
            storey -= (storey % 10)
        else:
            if (storey // 10) % 10 >= 5:
                storey += 10
            answer += t

        storey //= 10

    return answer