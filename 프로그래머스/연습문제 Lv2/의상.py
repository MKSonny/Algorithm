cnt = 0
calc = {}


def solution(clothes):
    answer = 0
    d = {}
    calc = {}
    maxx = -1
    for_incase = 0
    for i in clothes:
        if d.get(i[1]) == None:
            d[i[1]] = 0
            if_only_one = i[1]

        d[i[1]] += 1
        maxx = max(d[i[1]], maxx)

    # print('maxx', maxx)

    if maxx == 1:
        return 2 ** len(d) - 1
    if len(d) == 1:
        return d[if_only_one]

    l = list(d.keys())

    def multi(li):
        global calc
        t = 1
        # li.sort()
        if calc.get(str(li)) == None:
            # calc[str(li)] = 0
            for i in li:
                t *= i
            calc[str(li)] = t
            return t
        else:
            return calc[str(li)]

    def combination(level, l, sol, d):
        global cnt

        if len(sol) == 1:
            # print(sol)
            cnt += sol[0]
        elif len(sol) > 1:
            # print(sol)
            cnt += multi(sol)

        for i in range(level, len(l)):
            sol.append(d[l[i]])
            combination(i + 1, l, sol, d)
            sol.pop()

    combination(0, l, [], d)

    return cnt