from collections import deque


def solution(numbers):
    answer = []

    def make(num):
        temp = list(map(int, bin(num)[2:]))

        flag_idx = -1

        for idx, i in enumerate(temp):
            if i == 0:
                flag_idx = idx

        if flag_idx == -1:
            temp = [1] + list(temp)
            temp[1] = 0
        else:
            temp[flag_idx] = 1
            if flag_idx + 1 < len(temp):
                temp[flag_idx + 1] = 0

        temp = deque(temp)

        total = 0

        idx = 0

        # print(temp)

        while temp:
            if temp.pop() == 1:
                total += 2 ** (idx)
            idx += 1
            # print(total)

        return total

    for num in numbers:
        answer.append(make(num))

    return answer