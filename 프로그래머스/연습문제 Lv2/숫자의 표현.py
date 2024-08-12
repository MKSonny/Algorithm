def solution(n):
    answer = 1
    t_l = []

    for j in range(1, n // 2 + 1):
        total = 0
        l = []
        for i in range(j, n):
            total += i
            # total > n 조건 검사하지 않아서 시간초과 발생함
            if total > n:
                break
            l.append(i)
            if total == n:
                t_l.append(l)
                break

    answer += len(t_l)

    return answer