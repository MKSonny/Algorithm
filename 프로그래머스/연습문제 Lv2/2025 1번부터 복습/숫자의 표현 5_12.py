def solution(n):
    answer = 0

    l = [i for i in range(1, n // 2 + 2)]
    # print(l)

    lt, rt = 0, 0

    total = 0

    while True:
        if total <= n and rt < len(l):
            total += l[rt]
            rt += 1
        elif total >= n and lt < len(l):
            total -= l[lt]
            lt += 1

        if lt == len(l) - 1: break

        if total == n:
            # print(lt, rt)
            answer += 1

    return answer + 1