import sys

n = int(sys.stdin.readline())
li = [0] * 10001

max_value = -1
max_index = 0

length = 0
begin = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    length = max(a, length)
    begin = min(a, begin)

    if max_value < b:
        max_value = b
        max_index = a

    li[a] = b

st = begin
max_st = 0

while st < max_index:
    if max_st < li[st]:
        max_st = li[st]

    li[st] = max_st
    st += 1

ed = length
max_ed = 0

while ed > max_index:
    if max_ed < li[ed]:
        max_ed = li[ed]

    li[ed] = max_ed
    ed -= 1


print(sum(li))