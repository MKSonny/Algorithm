from itertools import combinations


def solution(orders, course):
    answer = []

    l = ''
    for i in orders:
        l += i
    l = list(set(list(l)))
    l.sort()

    for i in range(len(orders)):
        t = list(orders[i])
        t.sort()
        orders[i] = t

    for c in course:
        d = {}
        maxx = -1
        for order in orders:
            t = combinations(order, c)
            for a in t:
                a = ''.join(a)
                if d.get(a) == None:
                    d[a] = 0
                d[a] += 1
                maxx = max(d[a], maxx)
        if maxx <= 1:
            continue
        for key in d.keys():
            if d[key] == maxx:
                answer.append(key)

    answer.sort()

    return answer