def solution(sequence, k):
    answer = []

    lt, rt = 0, 0

    total = 0

    while True:

        while rt < len(sequence):
            total += sequence[rt]
            rt += 1
            if total >= k:
                break

        if total == k:
            answer.append((lt, rt - 1))

        while lt < len(sequence):
            total -= sequence[lt]
            lt += 1
            if total <= k:
                break

        if lt >= rt: break

        if total == k:
            answer.append((lt, rt - 1))

    answer.sort(key=lambda o: (o[1] - o[0]))

    return answer[0]