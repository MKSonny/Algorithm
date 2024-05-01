def solution(citations):
    answer = 0
    # citations = [4]
    lt, rt = 0, max(citations)

    max_h = -1

    while rt >= lt:
        mid = (lt + rt) // 2
        cnt = 0
        for i in citations:
            if i >= mid:
                cnt += 1
        if cnt >= mid:
            max_h = max(mid, max_h)
            # print(mid)
            lt = mid + 1
        else:
            rt = mid - 1

    return max_h