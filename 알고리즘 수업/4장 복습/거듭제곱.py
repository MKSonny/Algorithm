def power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    elif n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x * x, (n - 1) // 2)

# print(power(5, 5))

def powerMat(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        return powerMat(muultMat(a, a), n // 2)
    else:
        return muultMat(a, powerMat(muultMat(a, a), (n - 1) // 2))

def muultMat(a, b):
    n = len(a)
    m = len(b)
    # a[i][j] * b[j][k] = c[i][k]
    temp = [([0] * len(b)) for _ in range(len(a))]
    for i in range(n):
        for j in range(len(a[0])):
            for k in range(len(b[0])):
                temp[i][k] += a[i][j] * a[j][k]
    return temp

def fib_mat(n):
    if n < 2:
        return n
    mat = [[1, 1], [1, 0]]
    result = powerMat(mat, n)
    return result[0][1]


print(fib_mat(5))