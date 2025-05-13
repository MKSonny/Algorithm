def solution(citations):
    answer = 0
    max_h = 0

    for h in range(0, 10000 + 1):
        h1 = 0
        h2 = 0

        for j in citations:
            if j >= h:
                h1 += 1
            if j <= h:
                h2 += 1

        if h1 >= h and h2 <= h:
            max_h = max(h, max_h)

    return max_h