# n = int(input())
#
# x = 64
# l = [64, 32, 16, 8, 4, 2, 1]
#
# cnt = 0
# for i in l:
#     if n - i < 0:
#         continue
#     else:
#         n -= i
#         cnt += 1
#
# print(cnt)

n = int(input())
l = bin(n)
cnt = 0

for i in l:
    # 항상 0b로 시작하기 때문에
    # 아래와 같이해도 정답
    # 0b에는 1이 없음
    # print(i)
    if i == '1':
        cnt += 1

print(cnt)