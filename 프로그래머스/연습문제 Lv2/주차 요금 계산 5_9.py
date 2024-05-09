import math


def solution(fees, records):
    answer = []
    d = {}
    d_time = {}
    # for record in records:
    #     print(record)

    for record in records:
        # print(record)
        time, car_number, went = record.split()
        # print(car_number)
        if went == 'IN':
            d[car_number] = time
            if d_time.get(car_number) == None:
                d_time[car_number] = 0
        else:
            in_time = d[car_number]
            in_hour, in_minute = map(int, in_time.split(':'))
            out_hour, out_minute = map(int, time.split(':'))

            total_hour = out_hour - in_hour
            total_minute = out_minute - in_minute
            total = total_hour * 60 + total_minute
            # total = fees[1] + math.ceil((total - fees[0]) / fees[2]) * fees[3]
            d_time[car_number] += total
            d.pop(car_number)

    # 당일 들어오고 나가지는 않은 차량들 목록
    for key in d.keys():
        hour, min = map(int, d[key].split(':'))
        total = (23 - hour) * 60 + 59 - min
        d_time[key] += total

    temp = list(d_time.items())
    temp.sort()

    for item in temp:
        if item[1] - fees[0] < 0:
            total = fees[1]
        else:
            total = fees[1] + math.ceil((item[1] - fees[0]) / fees[2]) * fees[3]
        answer.append(total)

    return answer