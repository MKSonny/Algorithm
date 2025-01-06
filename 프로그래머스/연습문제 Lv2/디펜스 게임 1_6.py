import heapq


def solution(n, k, enemy):
    answer = 0

    h = []
    total = 0

    for i in enemy:
        heapq.heappush(h, -i)
        total += i
        if total > n:
            if k == 0:
                break
            k -= 1
            a = heapq.heappop(h)
            total += a
        answer += 1

    return answer