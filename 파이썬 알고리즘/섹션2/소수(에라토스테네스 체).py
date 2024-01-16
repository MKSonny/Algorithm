n = int(input())

def finding(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    return cnt == 2

total = 0

for i in range(1, n + 1):
    if finding(i):
        total += 1

print(total)