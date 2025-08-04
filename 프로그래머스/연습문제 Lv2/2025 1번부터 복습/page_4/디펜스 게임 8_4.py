def solution(n, k, enemy):
    answer = 0

    if k == 0:
        return 1
    if k == len(enemy):
        return len(enemy)

    cnt_1 = 1
    cnt_2 = 1

    n_1 = n
    n_2 = n

    k_1 = k - 1
    k_2 = k

    # print(n_1, k_1, cnt_1)

    # 처음 k 무조건 사용
    if k_1 >= 0:
        for i in range(1, len(enemy)):
            if n_1 <= 0:
                break

            cnt_1 = i + 1

            if n_1 - enemy[i] <= 0:
                k_1 -= 1
                if k_1 <= 0:
                    break
            else:
                n_1 -= enemy[i]

    # print(n_2, k_2, cnt_2)

    n_2 -= enemy[0]

    if n_2 > 0:
        for i in range(1, len(enemy)):
            if n_2 <= 0:
                break

            cnt_2 = i + 1

            if n_2 - enemy[i] <= 0:
                k_2 -= 1
                if k_2 <= 0:
                    break
            else:
                n_2 -= enemy[i]

    # print(cnt_1, cnt_2)
    return max(cnt_1, cnt_2)