def solution(n, a, b):
    answer = 1

    # 1 2 3 4 5 6 7 8
    # 7 // 2 = 3
    # 8 // 2 = 4
    # if 7 % 2 != 0:
    # 7 // 2 + 1
    #
    # 1 2 3 4
    # a = 2, b = 4
    # if a % 2 != 0:
    # then t_a = a + 1
    # if b % 2 != 0:
    # then t_b = b + 1
    # if t_a == t_b:
    # then return cnt
    cnt = 0
    if a % 2 != 0:
        t_a = a + 1
    else:
        t_a = a
    if b % 2 != 0:
        t_b = b + 1
    else:
        t_b = b

    while t_a != t_b:
        answer += 1

        if a % 2 != 0:
            a = a // 2 + 1
        else:
            a //= 2
        if b % 2 != 0:
            b = b // 2 + 1
        else:
            b //= 2
        if a % 2 != 0:
            t_a = a + 1
        else:
            t_a = a
        if b % 2 != 0:
            t_b = b + 1
        else:
            t_b = b

    return answer