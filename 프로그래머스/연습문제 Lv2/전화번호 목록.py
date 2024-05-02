def solution(phone_book):
    n = len(phone_book)
    for i in range(n - 1):
        for j in range(i + 1, n):
            str_1 = phone_book[i]
            str_2 = phone_book[j]
            fp = 0
            sp = 0
            while sp < len(str_2):
                if str_1[fp] == str_2[sp]:
                    fp += 1
                    sp += 1
                    if fp == len(str_1):
                        return False
                else:
                    sp += 1

    answer = True
    return answer