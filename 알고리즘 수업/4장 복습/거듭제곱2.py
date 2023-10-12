def power(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x * x, (n - 1) // 2)

print(power(5, 10))