from collections import Counter


def solution(k, tangerine):
    answer = 0

    l = dict(Counter(tangerine))
    keys = l.keys()
    to_sort = []

    for i in keys:
        to_sort.append((l[i], i))
    to_sort.sort(reverse=True)

    for value, key in to_sort:
        if value > k:
            k = 0
        else:
            k -= value
        answer += 1
        if k == 0:
            return answer

    return answer