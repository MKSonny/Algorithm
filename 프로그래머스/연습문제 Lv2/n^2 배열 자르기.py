def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        i = i + 1
        if i % n == 0:
            answer.append(n)
        else:
            answer.append(max((i // n) + 1, i % n))

    return answer