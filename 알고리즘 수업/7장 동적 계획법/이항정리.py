def bino_coef_dc(n, k):
    if k == 0 or k == n:
        return 1
    return bino_coef_dc(n - 1, k - 1) + bino_coef_dc(n - 1, k)