def solution(board, skill):
    answer = 0

    temp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(temp)):
        temp[i].append(0)

    temp.append([0 for _ in range(len(temp[0]))])

    for i in skill:
        t, a, b, c, d, degree = i

        if t == 1:
            temp[a][b] -= degree
            temp[c + 1][b] += degree
            temp[c + 1][d + 1] -= degree
            temp[a][d + 1] += degree
        else:
            temp[a][b] += degree
            temp[c + 1][b] -= degree
            temp[c + 1][d + 1] += degree
            temp[a][d + 1] -= degree

        # for i in temp:
        #     print(i)
        # print()

    # print('ori')
    # for i in temp:
    #     print(i)
    # print()

    for j in range(len(temp[0])):
        for i in range(len(temp) - 1):
            temp[i + 1][j] += temp[i][j]

    # for i in temp:
    #     print(i)
    # print()

    for i in range(len(temp)):
        for j in range(len(temp[0]) - 1):
            temp[i][j + 1] += temp[i][j]

    # print()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if temp[i][j] + board[i][j] > 0:
                answer += 1

    return answer