def solution(str1, str2):
    answer = 0

    a = ord('A')
    z = ord('Z')

    str1 = list(str1)
    str2 = list(str2)

    for i in range(len(str1)):
        str1[i] = str1[i].upper()

    for i in range(len(str2)):
        str2[i] = str2[i].upper()

    def check(ato):
        fi = []
        for i in range(len(ato) - 2 + 1):
            tm = ato[i:i + 2]
            # print(tm)
            f = ord(tm[0]) < a or ord(tm[0]) > z
            s = ord(tm[-1]) < a or ord(tm[-1]) > z

            if f or s: continue
            fi.append(''.join(tm))

        return fi

    p1 = check(str1)
    p2 = check(str2)

    p1.sort()
    p2.sort()

    # print(p1)
    # print(p2)

    def make_di(p):
        di = {}
        for i in p:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1

        return di

    di1 = make_di(p1)
    di2 = make_di(p2)

    # print(di1)
    # print(di2)
    # print(len(di1), len(di2))

    if len(di1) < len(di2):
        di1, di2 = di2, di1

    te = 0
    ke = []

    for i in di1:
        if i in di2:
            # te.append((i, max(di1[i], di2[i])))
            te += max(di1[i], di2[i])
            ke.append(i)
        else:
            # te.append((i, di1[i]))
            te += di1[i]

    for i in di2:
        if i not in ke:
            te += di2[i]

    co = 0

    for i in di1:
        if i in di2:
            co += min(di1[i], di2[i])
            # co.append((i, min(di1[i], di2[i])))
        # else:
        # co += di1[i]
        # co.append((i, di1[i]))

    #     print(te)
    #     print(co)

    if te == co: return 65536

    answer = int((co / te) * 65536)

    return answer