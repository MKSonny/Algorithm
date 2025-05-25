import sys

n = int(sys.stdin.readline())

# 1 1 -> 1
# 1 2 1 -> 2
# 1 3 3 1 -> 3
# 1 4 6 4 1 -> 4
# 1 5 10 10 5 1
l = [2, 4, 8, 16, 32]
print(2 ** n)