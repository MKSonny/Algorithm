from collections import Counter


def solution(phone_book):
    n = len(phone_book)

    phone_book.sort(key=lambda o: len(o))

    for i in range(n - 1):
        for j in range(i + 1, n):
            str_1_cnt = Counter(phone_book[i])
            str_2_cnt = Counter(phone_book[j])
            if len(str_1_cnt - str_2_cnt) > 0:
                continue
            str_1 = phone_book[i]
            str_2 = phone_book[j]
            n_1 = len(str_1)
            n_2 = len(str_2)
            for k in range(n_2 - n_1 + 1):
                if str_2[i:i + n_1] == str_1:
                    return False
    answer = True
    return answer