from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        can = []
        for order in orders:
            for i in combinations(order, c):
                can.append(''.join(sorted(i)))
        sorted_counter = Counter(can).most_common()
        answer += [menu for menu, cnt in sorted_counter if cnt > 1 and cnt == sorted_counter[0][1]]

    return sorted(answer)