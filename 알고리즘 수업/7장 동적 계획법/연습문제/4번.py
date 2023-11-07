def bino_coef_dp(n, k):
    C = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]

def bino_coef_mem(n, k):
    if C[n][k] == None :
        if k == 0 or k == n:
            C[n][k] = 1
    else :
        C[n][k] = bino_coef_mem(n-1 , k-1) + bino_coef_mem(n-1 , k)
    return C[n][k]

print(bino_coef_dp(6, 3))