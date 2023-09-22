n = 3
m = 2
ch = [0] * 10
cnt = 0
res = [0] * 10

def dfs(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        # i = 1 ~ 3
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                dfs(L + 1)
                ch[i] = 0
dfs(0)