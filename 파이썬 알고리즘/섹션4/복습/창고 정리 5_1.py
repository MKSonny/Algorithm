n = int(input())
l = list(map(int, input().split()))
m = int(input())

'''
10 
69 42 68 76 40 87 14 65 76 81
50
'''

for i in range(m):
    l.sort()
    l[0] += 1
    l[-1] -= 1

# print(l)
print(max(l) - min(l))