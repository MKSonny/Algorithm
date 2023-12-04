def hi(val, wt, W, n):
    table = [[0 for _ in range(W)] for _ in range(n + 1)]
#ㅏㅏ
    for i in range(1, n + 1):
        for w in range(1, W):
            if wt[i - 1] > w:
                table[i][w] = table[i - 1][w]
            else:
                valWith = val[i - 1] + table[i - 1][w - wt[i - 1]]
                valWithout = table[i - 1][w]
                table[i][w] = max(valWith, valWithout)

    return table[n][W - 1]

n = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))
total_hp = 100

print(hi(happy, hp, total_hp, n))