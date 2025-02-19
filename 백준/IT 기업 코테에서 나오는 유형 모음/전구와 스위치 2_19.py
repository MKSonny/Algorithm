import sys
# sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().strip()))
want = list(map(int, sys.stdin.readline().strip()))

dx = [-1, 0, 1]
min_cnt = float('inf')
flag = False

# dfs에 visited를 줄 수 없어 어려움

def dfs(temp, level, cnt):
    cnt += 1
    if temp == want:
        # print('temp', temp, cnt)
        return True

    if level == n or level < 0:
        return


    for i in range(3):
        nx = level + dx[i]
        if 0 <= nx < n:
            if temp[nx] == 1:
                temp[nx] = 0
            else:
                temp[nx] = 1

    print(level, temp, cnt)
    dfs(temp, level - 1, cnt)
    # dfs(temp, level, cnt)
    dfs(temp, level + 1, cnt)

dfs(li, 0, 0)
# if flag == False:
#     print(-1)
# else:
#     print(min_cnt)