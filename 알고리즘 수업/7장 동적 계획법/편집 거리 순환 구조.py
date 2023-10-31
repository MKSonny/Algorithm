S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)

mem = [[None for _ in range(n)] for _ in range(m)]

def edit_distance_mem(S, T, m, n, mem):
    if m == 0:
        return n
    if n == 0:
        return m

    if mem[m - 1][n - 1] == None:
        if S[m - 1] == T[n - 1]:
            mem[m - 1][n - 1] = edit_distance_mem(S, T, m - 1, n - 1, mem)
        else:
            mem[m - 1][n - 1] = min(edit_distance_mem(S, T, m - 1, n - 1, mem),
                                    edit_distance_mem(S, T, m, n - 1, mem),
                                    edit_distance_mem(S, T, m - 1, n, mem)) + 1

    return mem[m - 1][n - 1]

print(edit_distance_mem(S, T, m, n, mem))

for row in mem:
    print(row)