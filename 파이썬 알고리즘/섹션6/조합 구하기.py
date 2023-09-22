number = 3
select = 2
ch = [0] * 10

def dfs(v):
    if v == number + 1:
        cnt = 0
        for i in range(1, number + 1):
            if ch[i] == 1:
                cnt += 1
        if cnt == 2:
            for i in range(1, number + 1):
                if ch[i] == 1:
                    print(i, end=' ')
            print()
    else:
        ch[v] = 1
        dfs(v + 1)
        ch[v] = 0
        dfs(v + 1)

dfs(1)