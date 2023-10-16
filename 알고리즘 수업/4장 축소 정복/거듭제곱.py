def power(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        # 짝수라면 n == 0이 될때까지 계속 x * x 연산 수행
        # n이 0이 되면 1을 리턴
        # 인줄 알았는데 10//2 = 5 홀수가 된다.
        return power(x * x, n // 2)
    else:
        # 4//2 = 2 여기서도 다시 짝수가 된다
        return x * power(x * x, (n - 1)//2)

print(2048 * 2049)