def decimal_print(num):
    for i in range(4):
        print(num // 10 ** i)
        # print((num//(10 ** i) % 10), end= ' ')
decimal_print(1234)