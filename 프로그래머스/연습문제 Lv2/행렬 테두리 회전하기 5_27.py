from collections import deque


def solution(rows, columns, queries):
    answer = []

    answer = []
    l = [[] for _ in range(rows)]
    cnt = 0

    for i in range(rows):
        for j in range(columns):
            cnt += 1
            l[i].append(cnt)

    # for i in l:
    #     print(i)

    '''
    j += 1
    i += 1
    j -= 1
    i -= 1
    '''
    # 2,2,5,4
    # (2, 5) (2, 4)
    # 1 ~ 4, 1 ~ 3

    d_i = [0, 1, 0, -1]
    d_j = [1, 0, -1, 0]

    '''
    1, 1 -> j +=1 -> if j == 3 i -= 1
    '''

    visited = {3: False, 4: False, 1: False}

    s = [8]
    y = 1
    x = 1
    toggle = 0
    cnt = 0

    def dfs(y, x, s):
        toggle = 0
        l[y][x] = s.popleft()
        while True:
            ny = y + d_i[toggle]
            nx = x + d_j[toggle]
            if 0 <= ny < rows and 0 <= nx < columns:
                if ny == q[0] - 1 and nx == q[1] - 1:
                    break
                l[ny][nx] = s.popleft()

                if ny == q[0] - 1 and nx == q[3] - 1:
                    toggle += 1
                if ny == q[2] - 1 and nx == q[3] - 1:
                    toggle += 1
                if ny == q[2] - 1 and nx == q[1] - 1:
                    toggle += 1

                x = nx
                y = ny
            else:
                toggle += 1

    for q in queries:
        toggle = 0
        y = q[0] - 1
        x = q[1] - 1
        s = deque([l[y][x]])

        ny = 0
        nx = 0
        # print(q[0] - 1, q[3] - 1)
        # print(q[3] - 1, q[3] - 1)
        # print(q[3] - 1, q[1] - 1)
        while True:
            cnt += 1
            ny = y + d_i[toggle]
            nx = x + d_j[toggle]
            if 0 <= ny < rows and 0 <= nx < columns:
                if ny == q[0] - 1 and nx == q[1] - 1:
                    break
                s.append(l[ny][nx])

                if ny == q[0] - 1 and nx == q[3] - 1:
                    # visited[nx] = True
                    toggle += 1
                if ny == q[2] - 1 and nx == q[3] - 1:
                    # visited[ny] = True
                    toggle += 1
                if ny == q[2] - 1 and nx == q[1] - 1:
                    # visited[ny] = True
                    toggle += 1

                x = nx
                y = ny
            else:
                toggle += 1
        s.appendleft(s.pop())
        # print('s', s)
        answer.append(min(s))
        dfs(q[0] - 1, q[1] - 1, s)
        # for i in l:
        #     print(i)
        # print()

    return answer