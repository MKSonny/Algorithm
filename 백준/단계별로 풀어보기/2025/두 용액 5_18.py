import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

l.sort()

# lt, rt = 0, len(l) - 1
#
# k = 0
#
# maxx = 100000000000
# prev = maxx
# al, ar = 0, 0
#
# '''
# 10
# -1 -2 3 2 10000 100020 29442 323134 2342134 10
#
# '''
# answer = []
# t_rt = len(l) - 1
# # print(l)
#
# # -100, -1, 5
# #  lt       rt
# #  lt   rt
#
# while lt < rt < len(l):
#
#     k = abs(l[lt] + l[rt])
#     # print(k, prev, l[lt], l[rt])
#
#     if k > prev:
#         lt += 1
#         rt += 1
#         prev = maxx
#         continue
#     else:
#         answer.append((k, l[lt], l[rt]))
#
#     prev = k
#     rt -= 1
#     if rt == -1: break
#
# answer.sort()
#
# a = answer[0]
# # print(answer)
#
# print(min(a[1], a[2]), max(a[1], a[2]))

start, end = 0, len(l) - 1
ans = abs(l[start] + l[end])
final = [l[start], l[end]]

while start < end:
    left = l[start]
    right = l[end]

    total = left + right

    if abs(total) < ans:
        ans = abs(total)
        final = [left, right]
        if ans == 0:
            break

    if total < 0:
        start += 1 # 합이 음수면 0에 가까워지기 위해 start + 1
    else:
        end -= 1 # 합이 양수면 end - 1

print(final[0], final[1])