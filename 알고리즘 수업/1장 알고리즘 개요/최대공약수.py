def gcd(a, b):
    a_list = []
    b_list = []
    for i in range(1, a + 1):
        if a % i == 0:
            a_list.append(i)

    for i in range(1, b + 1):
        if b % i == 0:
            b_list.append(i)

    n = len(a_list)
    m = len(b_list)
    same = []

    for i in range(m):
        for j in range(n):
            if b_list[i] == a_list[j]:
                same.append(b_list[i])
                continue
    print(same)
    print(same[-1])

# 한 수의 약수만 구하는 방법
def gcd_one(a, b):
    a_list = []

    for i in range(a + 1, 0, -1):
        if a % i == 0 and b % i == 0:
            print(i)
            break

    # print(a_list)

# gcd 모법 답안
def gcd_answer(a, b):
    if a > b:
        min = b
    for i in range(min, 0, -1):
        if a % i == 0 and b % i == 0:
            print(i)
            break

# gcd(60, 28)
# gcd_one(60, 28)
gcd_answer(60, 28)