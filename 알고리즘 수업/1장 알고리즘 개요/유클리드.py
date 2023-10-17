def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def gcd_find(a, b):
    al = []
    bl = []

    for i in range(1, a + 1):
        if a % i == 0:
            al.append(i)

    for j in range(1, b + 1):
        if b % j == 0:
            bl.append(j)

    print(al, bl)

gcd_find(90, 80)
print(gcd(90, 80))