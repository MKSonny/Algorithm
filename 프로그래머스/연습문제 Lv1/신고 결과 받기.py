def solution(id_list, report, k):
    answer = [0] * len(id_list)
    warn = {}

    l = [set() for _ in range(len(id_list))]

    d = {}

    for idx, key in enumerate(id_list):
        d[key] = idx
        warn[idx] = 0

    for r in report:
        by, to = r.split()
        l[d[by]].add(d[to])

    # print(l)

    for i in l:
        for a in i:
            warn[a] += 1

    for key in warn:
        if warn[key] >= k:
            warn[key] = 1
        else:
            warn[key] = 0

    # for key in id_list:
    #     d[key] = 0

    #     print(d)
    #     print(warn)
    # print(warn)
    for idx, i in enumerate(l):
        for k in i:
            if warn[k]:
                answer[idx] += 1

    # print(d)
    # print(warn)

    return answer