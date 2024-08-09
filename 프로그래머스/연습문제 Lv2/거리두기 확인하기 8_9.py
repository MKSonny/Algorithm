def solution(places):
    answer = []

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def bfs(place, y, x):
        visited = [[False for _ in range(5)] for _ in range(5)]
        q = []
        q.append((y, x))
        ori_y, ori_x = y, x
        flag = True

        while q:
            y, x = q.pop(0)
            visited[y][x] = True

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < 5 and 0 <= nx < 5:
                    if not visited[ny][nx]:
                        if place[ny][nx] != 'X' and (abs(ori_y - ny) + abs(ori_x - nx)) <= 2:
                            if place[ny][nx] == 'P':
                                flag = False
                            q.append((ny, nx))

        return flag

    # temp = places[0]

    for temp in places:
        t_f = True
        for i in range(5):
            if t_f == False:
                break
            for j in range(5):
                if temp[i][j] == 'P':
                    if bfs(temp, i, j) == False:
                        answer.append(0)
                        t_f = False
                        break
        if t_f:
            answer.append(1)

    return answer