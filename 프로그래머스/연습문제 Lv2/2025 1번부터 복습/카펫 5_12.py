def solution(brown, yellow):
    answer = []

    for i in range(3, 10000):
        for j in range(3, 10000):
            y = (i - 2) * (j - 2)
            b = i * j - y
            if y == yellow and b == brown:
                return [j, i]

    return answer