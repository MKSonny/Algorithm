def binary(n):
    cnt = 0
    while n != 0:
        n = n // 2
        cnt += 1
    return cnt

print(binary(65))