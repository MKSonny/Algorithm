def solution(n):
    answer = 0

    def count(number):
        cnt = 0

        while number:
            if number % 2 == 1:
                cnt += 1
            number //= 2

        return cnt

    a = count(n)

    for i in range(n + 1, 1000000):
        if a == count(i):
            return i

    return answer