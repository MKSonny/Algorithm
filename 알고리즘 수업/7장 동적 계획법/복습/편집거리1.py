S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)

mem = [[None] * n for _ in range(m)]

def edit_distance(S, T, m, n, mem):
    if n == 0:
        return m
    if m == 0:
        return n

    for i in range(m):
        for j in range(n):
            if S[i - 1] == T[j - 1]:
