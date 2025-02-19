import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(sys.stdin.readline().rstrip())

li = list(set(li))

li.sort(key=lambda o: (len(o), o))

for i in li: print(i)