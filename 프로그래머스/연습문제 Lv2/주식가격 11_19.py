from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    cnt = 0

    while prices:
        p = prices.popleft()
        cnt = 0
        for i in prices:
            cnt += 1
            if p > i:
                break
        answer.append(cnt)

    return answer