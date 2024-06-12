from itertools import permutations


def solution(numbers):
    answer = 0

    l = list(numbers)
    test = set()

    for i in range(1, len(l) + 1):
        t = permutations(l, i)
        for a in t:
            a = int(''.join(a))
            # print(a)
            if a == 0 or a == 1:
                continue
            test.add(a)
    test = list(test)
    test.sort()

    # print(test)

    for i in test:
        a = i // 2
        flag = False
        for k in range(2, a + 1):
            if i % k == 0:
                flag = True
                break
        if flag:
            continue
        else:
            answer += 1
    # print(test)

    return answer