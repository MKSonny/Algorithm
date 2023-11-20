S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)

mem = [[None] * n for _ in range(m)]

def edit_distance(S, T, m, n, mem):
    if m == 0:
        return n
    if n == 0:
        return m

    if S[m - 1] == T[n - 1]:
        mem[m - 1][n - 1] = edit_distance(S, T, m - 1, n - 1, mem)
    else:
        mem[m - 1][n - 1] = min(
            edit_distance(S, T, m - 1, n - 1, mem),
            edit_distance(S, T, m, n - 1, mem),
            edit_distance(S, T, m - 1, n, mem)
        ) + 1

    return mem[m - 1][n - 1]

print(edit_distance(S, T, m, n, mem))

for i in mem:
    print(i)