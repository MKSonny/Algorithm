string_a = list('ABCDEF')
string_b = list('GBCDFE')

n = len(string_a)
lcs = [[0]*(n + 1) for _ in range(n + 1)]
# print(lcs)

for j in range(len(string_a)):
    for i in range(len(string_b)):
        if i == 0 or j == 0:
            lcs[i][j] = 0
        elif string_a[i] == string_b[j]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

for i in range(n + 1):
    for j in range(n + 1):
        print(lcs[j][i], end=' ')
    print()

result = []
def lcs_dp(x, y):
    m = len(x)
    n = len(y)
    L = [[None]*(n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L

def lcs_search():
    

lcs = lcs_dp(string_a, string_b)
print(lcs)