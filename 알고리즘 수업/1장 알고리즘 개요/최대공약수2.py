def gcd(a, b):
    list_a = []
    list_b = []
    for i in range(1, a + 1):
        if a % i == 0:
            list_a.append(i)

    for i in range(1, b + 1):
        if b % i == 0:
            list_b.append(i)

    print(list_a)
    print(list_b)

gcd(12, 18)