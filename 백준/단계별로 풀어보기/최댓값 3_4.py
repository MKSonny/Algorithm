import sys

maxx = -1
maxx_i = -1
for i in range(9):
    n = int(sys.stdin.readline())
    if n > maxx:
        maxx_i = i + 1
        maxx = n

print(maxx)
print(maxx_i)