def solution(park, routes):
    answer = []

    dict = {'S': 1, 'N': 0, 'W': 2, 'E': 3}

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    H = len(park)
    W = len(park[0])

    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                y, x = i, j
                break

    while routes:
        go_to, num = routes.pop(0).split()
        i = dict[go_to]
        t = True

        for k in range(1, int(num) + 1):
            ny = y + (dy[i] * k)
            nx = x + (dx[i] * k)
            if 0 <= ny < H and 0 <= nx < W:
                if park[ny][nx] == 'X':
                    t = False
                    break
            else:
                t = False
                break
        if t:
            print(ny, nx)
            y, x = ny, nx

    answer = [y, x]
    return answer