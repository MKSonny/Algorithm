def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]

    y = -1
    x = 0
    cnt = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1
                x -= 1
            answer[y][x] = cnt
            cnt += 1

    temp = []
    for i in answer:
        for k in i:
            temp.append(k)

    return temp