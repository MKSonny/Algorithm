def solution(sequence, k):
    answer = []

    n = len(sequence)
    l = []

    lt, rt = 0, 0

    answer = [0, n]
    t = sequence[lt]

    while True:
        if t < k:
            rt += 1
            if rt == n:
                break
            t += sequence[rt]
        else:
            if t == k:
                if rt - lt < answer[1] - answer[0]:
                    answer = [lt, rt]
                    # lt = 2, rt = 3
            t -= sequence[lt]
            lt += 1

    return answer