def solution(n, a, b):
    answer = 0

    while True:
        answer += 1

        if a // 2 + a % 2 == b // 2 + b % 2:
            break

        a = a // 2 + a % 2
        b = b // 2 + b % 2

    return answer