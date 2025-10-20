def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        start_price = prices[i]
        cnt = 0

        for j in range(i + 1, len(prices)):
            cnt += 1

            if start_price > prices[j]:
                break
        answer.append(cnt)

    answer.append(0)

    return answer