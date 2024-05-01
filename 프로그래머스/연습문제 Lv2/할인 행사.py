def solution(want, number, discount):
    answer = 0
    d = {}

    for w, n in zip(want, number):
        d[w] = n

    w_s = set(want)

    cnt = 0

    # print(len(discount))
    # print(discount[5:15])
    for i in range(len(discount)):
        l = discount[i:i + 10]
        # print(l)
        a = {}

        flag = True

        for item in l:
            # if item in w_s:
            # print(item, item in w_s)
            if a.get(item) == None:
                a[item] = 0
            a[item] += 1
            # else:
            # flag = False
            # break

        if flag:
            for w in want:
                if a.get(w) == None:
                    flag = False
                    break
                if a[w] < d[w]:
                    flag = False
                    break
        else:
            continue

        if flag:
            cnt += 1
            # print(i, cnt)
            # return i + 1

    return cnt