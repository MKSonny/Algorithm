import heapq


def solution(scoville, K):
    answer = 0

    h = []

    for i in scoville:
        heapq.heappush(h, i)

    cnt = 0

    while heapq:
        f = heapq.heappop(h)

        if len(h) == 0:
            if f >= K:
                return cnt
            else:
                return -1

        if f >= K:
            return cnt
        cnt += 1

        s = heapq.heappop(h) * 2
        heapq.heappush(h, f + s)

    if cnt == 0:
        return -1