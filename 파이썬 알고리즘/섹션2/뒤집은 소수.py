n = int(input())
l = list(map(int, input().split()))

def reverse(x):
    tmp = 0
    while x >= 10:
        c = x % 10
        tmp += c
        tmp *= 10
        x //= 10
    c = x % 10
    tmp += c
    return tmp

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for value in l:
    reversed = reverse(value)
    if isPrime(reversed):
        print(reversed, end=' ')
