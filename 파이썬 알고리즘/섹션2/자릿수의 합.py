n = int(input())
l = list(input().split())
'''
3
125 15232 97
'''
max = -float('inf')
max_i = 0

for i in range(n):
    tmp = list(map(int, l[i]))
    if sum(tmp) > max:
        max = sum(tmp)
        max_i = i

print(l[max_i])