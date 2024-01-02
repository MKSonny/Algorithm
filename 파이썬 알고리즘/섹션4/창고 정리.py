n = int(input())
l = list(map(int, input().split()))
m = int(input())

'''
10
69 42 68 76 40 87 14 65 76 81
50
'''

l.sort()

# print(l)

for _ in range(m):
    l[0] += 1
    l[n - 1] -= 1
    l.sort()

print(l[n - 1] - l[0])