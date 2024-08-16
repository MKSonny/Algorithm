from collections import Counter


def solution(k, tangerine):
    answer = 0
    tangerine.sort()

    # print(tangerine[n - k:])
    l = Counter(tangerine)
    t = []
    for i in l.items():
        t.append(i)
    t.sort(key=lambda o: o[1])

    temp = []
    for a, b in t:
        ll = [a] * b
        for i in ll:
            temp.append(i)

    return len(set(temp[-k:]))