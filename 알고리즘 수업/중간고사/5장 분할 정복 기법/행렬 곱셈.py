def powerMat(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        return powerMat(multiMat(a, a), n // 2)
    else:
        return multiMat(a, (powerMat(multiMat(a, a), (n - 1) // 2)))

def fibo(n):
    if n < 2:
        return n
    mat = [[1, 1], [1, 0]]
    result = powerMat(mat, n)
    return result[0][1]

def multiMat(a, b):
    temp = [([0] * len(b[0])) for _ in range(len(a))]
    # k = 0
    sum = 0

    for i in range(len(a)):
        for k in range(len(b[0])):
            for j in range(len(a[0])):
                sum += a[i][j] * b[j][k]
                # print(a[i][j], b[j][k], end=' + ')

            temp[i][k] = sum
            sum = 0
            # print(', ', end='')
    # for row in temp:
    #     print(row)
    return temp

a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6, 7],
    [8, 9, 10]
]

print(fibo(9))