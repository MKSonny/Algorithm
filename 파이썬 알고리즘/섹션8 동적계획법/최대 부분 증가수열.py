import sys

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))
dy = [0] * n

'''
8
5 3 7 8 6 2 9 4
'''

for i in range(n):
    j = i
    maxx = 0
    while j >= 0:
        if l[j] < l[i]:
            if maxx < dy[j]:
                maxx = dy[j]
        j -= 1
    dy[i] = maxx + 1

print(max(dy))