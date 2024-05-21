def solution(n):
    answer = ''
    result = []
    while n:
        t = n % 3
        if t == 0:
            t = 4
            n -= 1
        result.append(str(t))
        n //= 3

    result = reversed(result)

    return answer.join(result)