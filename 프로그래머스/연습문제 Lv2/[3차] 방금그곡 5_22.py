from collections import Counter
from datetime import datetime


def solution(m, musicinfos):
    answer = ''

    def my_counter(l):
        n = len(l)
        if n == 1:
            return Counter(l)
        prev = 0
        idx = 1
        d = {}
        while idx < n:
            if l[idx] != '#':
                if d.get(l[prev]) == None:
                    d[l[prev]] = 1
                else:
                    d[l[prev]] += 1
            else:
                if d.get(l[prev] + l[idx]) == None:
                    d[l[prev] + l[idx]] = 1
                else:
                    d[l[prev] + l[idx]] += 1
                prev = idx + 1
                idx += 2
                continue
            idx += 1
            prev += 1
        if d.get(l[prev]) == None:
            d[l[prev]] = 1
        else:
            d[l[prev]] += 1

        return d

    heard_melody = Counter(my_counter(list(m)))
    # print('heard_melody', heard_melody)

    for i in musicinfos:
        split_l = list(i.split(','))

        time_format = "%H:%M"
        start_time = datetime.strptime(split_l[0], time_format)
        end_time = datetime.strptime(split_l[1], time_format)

        time = int((end_time - start_time).total_seconds() / 60)
        # print(time)

        l = split_l[3]

        radio = Counter(my_counter(l))
        # print(radio)
        n = sum(radio.values())

        temp = ''
        if time < n:
            temp = l[:time]
        else:
            # print('calc', time // n)
            for _ in range(time // n):
                temp += l
            temp += l[:time % n]

        radio = Counter(my_counter(list(temp)))
        print(radio)
        # {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1}
        # print('radio', radio)
        if len(heard_melody - radio) == 0:
            return split_l[2]

    return "(None)"