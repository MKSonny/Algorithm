def solution(n):
    answer = 0
    temp = []

    t_n = n

    ori_cnt = 0

    while n > 0:
        if n % 2 == 1:
            ori_cnt += 1
        n //= 2

    for i in range(t_n + 1, 1000000):
        cnt = 0
        flag = False
        temp = i
        while i > 0:
            if i % 2 == 1:
                cnt += 1
            if cnt > ori_cnt:
                break
            i //= 2

        if cnt == ori_cnt:
            return temp

    return answer