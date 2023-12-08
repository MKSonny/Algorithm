# 이항정리
def bino_coef_dc(n, k):
    if k == 0 or k == n:
        return 1
    return bino_coef_dc(n - 1, k - 1) + bino_coef_dc(n - 1, k)

def bino_coef_dp(n, k):
    C = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            # else문이 없을 경우 아래가 무조건 실행되서
            # i = 0, j = 0 일 떄
            # 이전 if문에서 table[0][0]을 1을 적어도
            # 여기서
            # table[0][0] = table[-1][-1] + table[-1][0]
            # table[0][0] = 0 + 0
            # 으로 값이 초기화되어 답이 안나온다.
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]

print(bino_coef_dc(4, 2))
print(bino_coef_dp(4, 2))