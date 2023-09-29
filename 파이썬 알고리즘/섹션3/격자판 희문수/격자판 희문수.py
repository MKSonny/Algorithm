import sys
sys.stdin = open('in1.txt', 'r')
a = [list(map(int, input().split())) for _ in range(7)]
# a = [1, 2, 3, 2, 1, 6, 1]
low = 0
high = 2

cnt = 0

for row in a:
    while row[low] != row[high] and high < 6:
        high += 1
    # print(high)
    while row[low] == row[high] and low < high:
        low += 1
        high -= 1
        if low == high:
            cnt += 1
            break
print(cnt)

# print(low, high)