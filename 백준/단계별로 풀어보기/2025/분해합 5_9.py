import sys

l = list(sys.stdin.readline().rstrip())

ori = int(''.join(l))

n = len(l)

temp = []

def check(k):
    total = 0
    for i in k:
        total += int(i)

    if int(''.join(k)) + total == ori:
        return True
    return False

def brute_force():
    for i in range(1, 1000000):
        if check(list(str(i))):
            return i
    return 0

def dfs(level):
    if level == n:
        if check(temp):
            print(''.join(temp))
        # print(temp)
        return
    for i in range(1, 10):
        temp.append(str(i))
        dfs(level + 1)
        temp.pop()

# dfs(0)
print(brute_force())