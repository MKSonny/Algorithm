S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)

mem = [[None for _ in range(n + 1)] for _ in range(m + 1)]

def edit_distance(S, T, m, n, mem):
    if mem[m][n] == None:
        if m == 0:
            return n
        if n == 0:
            return m

        if S[m - 1] == T[n - 1]:
            mem[m][n] = edit_distance(S, T, m - 1, n - 1, mem)
        else:
            mem[m][n] = min(
                edit_distance(S, T, m - 1, n - 1, mem),
                edit_distance(S, T, m, n - 1, mem),
                edit_distance(S, T, m, n - 1, mem)
            ) + 1
    return mem[m][n]

print(edit_distance(S, T, m, n, mem))