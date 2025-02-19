import sys
# sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
bulb = list(map(int, sys.stdin.readline().strip()))
target = list(map(int, sys.stdin.readline().strip()))

def change(A, B):
    A_copy = A[:]
    press = 0
    for i in range(1, n):
        if A_copy[i - 1] == B[i - 1]:
            continue
        press += 1
        for j in range(i - 1, i + 2):
            if j < n:
                A_copy[j] = 1 - A_copy[j]