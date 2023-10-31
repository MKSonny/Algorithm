def edit_distance(S, T, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if S[m - 1] == T[n - 1]:
        return edit_distance(S, T, m - 1, n - 1)

    return 1 + min(edit_distance(S, T, m, n - 1),  # 삽입
                   edit_distance(S, T, m - 1, n),  # 삭제
                   edit_distance(S, T, m - 1, n - 1))  # 대체
