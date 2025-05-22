import sys

l = list(sys.stdin.readline().rstrip())

nums = {'c': 26, 'd': 10}
n = len(l)
res = nums[l[0]]

for i in range(1, n):
    mul = nums[l[i]]
    if l[i] == l[i - 1]:
        mul -= 1
    res *= mul

print(res)