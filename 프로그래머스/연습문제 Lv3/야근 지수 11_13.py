import heapq

def solution(n, works):
    answer = 0
    h = []
    for i in works:
        heapq.heappush(h, -i)

    for i in range(n):
        if len(h) == 0:
            return 0
        t = heapq.heappop(h)
        if t == 0:
            continue
        heapq.heappush(h, t + 1)

    for i in h:
        answer += i ** 2

    return answer