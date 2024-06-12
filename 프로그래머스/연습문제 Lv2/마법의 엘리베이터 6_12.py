def solution(storey):
    answer = 0
    while storey != 0:
        # 2550
        t = 10 - (storey % 10)
        if storey % 10 >= 5:
            storey += t
            answer += t
        else:
            answer += (storey % 10)
            storey -= (storey % 10)
        storey //= 10

    return answer