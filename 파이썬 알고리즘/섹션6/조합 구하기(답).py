select = 2
n = 4
res = [0] * 2

def dfs(l, s):
    if l == select:
        for i in res:
            print(i, end=' ')
        print()
    else:
        for i in range(s, n + 1):
            # == dfs(0, 1) ==
            # i = 1, l = 0, s = 1
            # res[0] = 1

            # i = 2, s = 1
            # res[0] = 2
            # dfs(1, 2) -> i + 1로 했다면 dfs(1, 3)
            # i = 2
            # res[1] = 2
            # 2 2 -> 출력


            # == dfs(1, 2) ==
            # s = 2, i = 2, l = 1
            # res[1] = 2

            # i = 3, l = 1
            # res[1] = 3

            # i = 4, l = 1
            # res[1] = 4
            res[l] = i

            # dfs(1, 2)
            # stack
            dfs(l + 1, i + 1)
dfs(0, 1)