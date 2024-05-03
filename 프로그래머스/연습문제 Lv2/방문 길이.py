def solution(dirs):
    answer = 0

    # dirs = "LULLLLLLUUUURL"

    l = [[0 for _ in range(11)] for _ in range(11)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    di = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    di_x = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

    y = 5
    x = 5
    l[y][x] = 1
    visited = set()

    for d in dirs:
        ny = y + dy[di[d]]
        nx = x + dx[di[d]]
        if 0 <= ny < 11 and 0 <= nx < 11:
            if (ny, nx, di_x[d]) in visited:
                # print(ny, nx, d)
                y = ny
                x = nx
            else:
                answer += 1
                # print(answer + 1, ny, nx, d)
                visited.add((y, x, d))
                visited.add((ny, nx, di_x[d]))
                # print(answer, visited)
                l[ny][nx] = 1
                y = ny
                x = nx

    # for i in l:
    #     print(i)
    # print()

    return answer