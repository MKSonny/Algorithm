def solution(diffs, times, limit):
    answer = []

    left = 1
    right = max(diffs)

    while left <= right:
        mid = (left + right) // 2
        time_prev = 0
        total = 0

        for i in range(len(diffs)):
            level = mid
            if diffs[i] > level:
                wrong = diffs[i] - level
                if i - 1 >= 0:
                    total += (times[i] + times[i - 1]) * wrong + times[i]
                else:
                    total += (0 + times[i]) * wrong + times[i]
            else:
                total += times[i]

        if total <= limit:
            right = mid - 1
            answer.append(mid)
        else:
            left = mid + 1

    return min(answer)