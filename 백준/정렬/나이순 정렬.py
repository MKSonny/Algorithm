import sys

input = sys.stdin.readline

n = int(input())

l = []

for _ in range(n):
    age, name = input().split()
    l.append((int(age), name))

l.sort(key=lambda o:o[0])

for k in l:
    print(k[0], k[1])