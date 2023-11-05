def multMat(a, b):
    total = [([0] * len(b[0])) for _ in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b[0])):
            sum = 0
            for j in range(len(a[0])):
                sum += a[i][j] * b[j][k]
                # print(a[i][j] * b[j][k])
            total[i][k] = sum

    return total

def powerMat(x, n):
    if n == 1:
        return x
    elif n %2 == 0:
        return powerMat(multMat(x, x), n // 2)
    else:
        return multMat(x, powerMat(multMat(x, x), (n - 1) // 2))


def powerFib(n):
    if n < 2:
        return n

    mat = [1, 1], [1, 0]
    result = powerMat(mat, n)
    return result[0][1]

a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6, 7],
    [8, 9, 10]
]
# 0 1 2 3 4 5 6 7 8
# 0 1 1 2 3 5 8 13 21
def multi_mat(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Invalid Matrix!")

    return [
        [
            sum([a[i][k] * b[k][j] for k in range(len(a[0]))])
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]

print(multMat(a, b))
print(multi_mat(a, b))