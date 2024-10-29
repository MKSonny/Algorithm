import math


def solution(fees, records):
    answer = []

    # print(fees)

    def calc_fee(time):
        if time < fees[0]:
            return fees[1]
        else:
            return fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]

    d = {}
    q = []
    total = {}

    def calc_time(time):
        hour, minute = time.split(':')
        hour, minute = int(hour), int(minute)
        return hour * 60 + minute

    for i in records:
        l = i.split()
        time, car_number, info = l[0], l[1], l[2]
        # print(time, car_number, info)
        if info == 'IN':
            if car_number not in total:
                total[car_number] = 0
            d[car_number] = calc_time(time)
        else:
            d[car_number] = calc_time(time) - d[car_number]
            total[car_number] += d[car_number]
            d.pop(car_number)

    for key in d.keys():
        total[key] += calc_time('23:59') - d[key]

    final = []

    for key in total.keys():
        total[key] = calc_fee(total[key])
        final.append((key, total[key]))

    final.sort()
    for a, b in final:
        answer.append(b)

    return answer