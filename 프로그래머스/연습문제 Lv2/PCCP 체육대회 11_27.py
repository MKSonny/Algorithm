from itertools import permutations


def solution(ability):
    answer = 0
    n, major = len(ability), len(ability[0])
    l = [i for i in range(1, n + 1)]
    p = permutations(l, major)

    for i in p:
        # print(i)
        score = 0
        for idx, j in enumerate(i):
            # print(idx, j)
            score += ability[j - 1][idx]
        answer = max(answer, score)

    return answer