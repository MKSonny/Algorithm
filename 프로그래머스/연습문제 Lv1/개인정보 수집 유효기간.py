import datetime as dt
from dateutil.relativedelta import relativedelta


def solution(today, terms, privacies):
    answer = []
    today = today.split('.')
    # print(today)
    for i in range(len(today)):
        today[i] = int(today[i])

    today = dt.datetime(today[0], today[1], today[2])

    d = {}

    for term in terms:
        t, m = term.split()
        m = int(m)
        d[t] = m

    for idx, item in enumerate(privacies):
        year, mounth, day_t = item.split('.')
        day, term = day_t.split()
        year, mounth, day = int(year), int(mounth), int(day)
        #         # d[term] # 6
        ti = dt.datetime(year, mounth, day) + relativedelta(months=d[term])
        if ti <= today:
            answer.append(idx + 1)

        # 한달이 무조건 30일이 아닐 수 있음
        # if ti.days > d[term] * 30:
        #     answer.append(idx + 1)

    return answer