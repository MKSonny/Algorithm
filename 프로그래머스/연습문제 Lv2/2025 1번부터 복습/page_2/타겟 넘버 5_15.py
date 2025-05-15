from collections import deque


def solution(numbers, target):
    answer = 0

    options = [0, 1]

    def check(l):
        total = 0

        for i in range(len(l)):
            if l[i] == 0:
                total -= numbers[i]
            else:
                total += numbers[i]

        return total

    def to_bi(num):
        q = deque([])

        while num:
            q.appendleft(num % 2)
            num //= 2

        for _ in range(len(numbers) - len(q)):
            q.appendleft(0)

        return q

    for i in range(2 ** len(numbers)):
        if check(to_bi(i)) == target:
            answer += 1

    return answer