import sys

l = [i for i in range(1, 31)]

for i in range(28):
    k = int(sys.stdin.readline())
    l.remove(k)

for i in l:
    print(i)