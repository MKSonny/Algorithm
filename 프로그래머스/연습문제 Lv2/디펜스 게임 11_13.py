import heapq

def solution(n, k, enemy):
    answer = 0
    h = []
    total_enemy = 0

    for e in enemy:
        total_enemy += e
        heapq.heappush(h, -e)
        if total_enemy > n:
            if k == 0:
                break
            total_enemy += heapq.heappop(h)
            k -= 1
        answer += 1

    return answer