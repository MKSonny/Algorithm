import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

def check(t):
    for i in range(2, t):
        if t % i == 0:
            return False
    return True


answer = 0

for i in l:
    if i == 1: continue
    if check(i):
        answer += 1

print(answer)