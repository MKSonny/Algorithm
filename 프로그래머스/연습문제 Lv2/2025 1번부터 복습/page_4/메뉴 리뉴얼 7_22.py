from itertools import combinations


def solution(orders, course):
    answer = []

    maxx = -1

    l = []

    for i in range(len(orders)):
        l.append(sorted(list(orders[i])))

    l.sort(key=lambda o: len(o))

    #     for i in range(len(l)):
    #         maxx = max(maxx, len(l[i]))

    #     s = set()

    #     for i in range(len(l)):
    #         for k in range(2, maxx + 1):
    #             if len(l[i]) < k:
    #                 continue
    #             for j in range(len(l[i]) - k + 1):
    #                 s.add(''.join(l[i][j:j + k]))

    #     s = list(s)
    #     s.sort(key=lambda o:len(o))

    # for i in l:
    #     print(i)

    di = {}
    di_len = {}

    for i in course:
        di_len[i] = 0

    # print(di_len)

    for i in l:
        for j in course:
            c = combinations(i, j)
            for k in c:
                # print(list(k))
                t = ''.join(list(k))
                if t not in di.keys():
                    di[t] = 1
                else:
                    di[t] += 1
                di_len[j] = max(di_len[j], di[t])

    for k in di.keys():
        if di[k] >= di_len[len(k)] and di[k] > 1:
            # print(k, di[k], di_len[len(k)])
            answer.append(k)

    answer.sort()


    return answer