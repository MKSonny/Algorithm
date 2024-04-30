import heapq


def solution(n, stations, w):
    answer = 0
    std = w * 2 + 1

    cnt = 0
    start = 0

    for station in stations:
        s = station - w
        e = station + w
        if s < 0:
            s = 0
        if e > n:
            e = n
        cnt = s - start - 1
        # print(s, start)
        start = e
        answer += cnt // std
        if cnt % std != 0:
            answer += 1


    if e != n:
        cnt = n - e
        answer += cnt // std
        if cnt % std != 0:
            answer += 1

    return answer