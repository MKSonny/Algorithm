import heapq


def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h, i)

    while h:
        f = heapq.heappop(h)
        if f >= K:
            return answer
        if len(h) == 0:
            return -1
        s = heapq.heappop(h)
        answer += 1

        result = f + s * 2
        heapq.heappush(h, result)

    return answer