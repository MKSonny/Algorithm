def find_max_hang_sum(A):
    n = len(A)
    max_hang = 0
    max_hang_yul = 0
    total = 0
    total_yul = 0
    total_cross_1 = 0
    total_cross_2 = 0
    for i in range(n):
        if max_hang < total:
            max_hang = total
        if max_hang_yul < total_yul:
            max_hang_yul = total_yul
        total = 0
        total_yul = 0
        total_cross_1 += A[i][i]
        total_cross_2 += A[i][n - i - 1]
        for j in range(n):
            total += A[i][j]
        for k in range(n):
            total_yul += A[k][i]
    # print('total_cross', total_cross_1)
    # print('total_cross', total_cross_2)
    # print(max_hang_yul)
    # print(max_hang)
    print(max(total_cross_1, total_cross_2, max_hang_yul, max_hang))

list = [
    [10, 13, 10, 12, 15],
    [12, 39, 30, 23, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19]
]
# find_max_hang_sum(list)