S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)

mem = [[None for _ in range(n)] for _ in range(m)]

def edit_distance(S, T, n, m, mem):
    if m == 0:
        return n
    if n == 0:
        return m

    if mem[m - 1][n - 1] == None:
        if S[m - 1] == T[n - 1]:
            mem[m - 1][n - 1] = edit_distance(S, T, n - 1, m - 1, mem)
        else:
            # 각각 무슨 행동인지, 삽입, 삭제, 교체?
            mem[m - 1][n - 1] = min(
                edit_distance(S, T, n - 1, m, mem),
                edit_distance(S, T, n, m - 1, mem),
                edit_distance(S, T, n - 1, m - 1, mem)
            ) + 1

    return mem[m - 1][n - 1]

print(edit_distance(S, T, n, m, mem))