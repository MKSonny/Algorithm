def solution(fees, records):
    answer = []

    di = {}

    def calc(enter, leave):
        e_h, e_m = map(int, enter.split(':'))
        l_h, l_m = map(int, leave.split(':'))

        e = e_h * 60 + e_m
        l = l_h * 60 + l_m

        # print(enter, leave)

        total = l - e

        return total

    #         print(total)

    def calc_price(total):
        price = fees[1]

        if total >= fees[0]:
            total -= fees[0]
        else:
            return fees[1]

        flag = total % fees[2]
        total //= fees[2]

        if flag > 0:
            total += 1

        price += total * fees[3]

        return price

    di_2 = {}

    for r in records:
        time, num, info = r.split()

        if info == 'IN':
            di[num] = time
            if num not in di_2.keys():
                di_2[num] = 0

        if info == 'OUT':
            # time - di[num]
            di_2[num] += calc(di[num], time)
            # print(num, calc(di[num], time))
            del (di[num])

        # print(di_2)

    # print(di)

    for k in di.keys():
        di_2[k] += calc(di[k], '23:59')
        # di[k]

    # print(di_2)
    keys = list(di_2.keys())
    keys.sort()

    for k in keys:
        answer.append(calc_price(di_2[k]))

    return answer