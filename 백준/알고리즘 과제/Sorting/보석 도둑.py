import heapq

n, m = map(int, input().split())

dia = []
bag = []


for _ in range(n):
    reverse = list(map(int, input().split()))
    # reverse[0], reverse[1] = reverse[1], reverse[0]
    heapq.heappush(dia, (-reverse[1], reverse[0]))


for _ in range(m):
    heapq.heappush(bag, -(int(input())))
    # bag.append()

max_val = 0

# 0, 1 1, 1 , 0, 1

# 먼저 다이아몬드의 가치를 높은 순으로 배치한다.
# 그리고 가방을 큰 무게 순으로 배치한다.
# 다이아몬드의 가치에 해당하는 무게와 가방을 비교하고 작으면 가방에 다이아몬드를 pop(0)한다.

# re_dia = []
max_take = 0
toggle = 0
cnt = 0

bag_value = -heapq.heappop(bag)

while True:
    dia_get = heapq.heappop(dia)
    dia_value = -dia_get[0]
    dia_weight = dia_get[1]

    toggle = 1
    # print(dia_value, dia_weight)

    if bag_value >= dia_weight:
        max_take += dia_value
        cnt += 1
        if cnt == m:
            break
        bag_value = -heapq.heappop(bag)
        # bag_value = -bag.pop()

print(max_take)

# for i in range(n - 1):
#     max_val = i
#     for j in range(i + 1, n):
#         if dia[j][1] > dia[max_val][1]:
#             max_val = j
#
#     dia[i], dia[max_val] = dia[max_val], dia[i]
#
# for i in range(m - 1):
#     max_val = i
#     for j in range(i + 1, m):
#         if bag[j] > bag[max_val]:
#             max_val = j
#
#     bag[i], bag[max_val] = bag[max_val], bag[i]

# max_take = 0

# print(dia)
# print(bag)
# i = 0
# j = 0
#
# while True:
#     if len(bag) == 0:
#         break
#
#     if bag[0] >= dia[j][0]:
#         max_take += dia.pop(0)[1]
#         bag.pop()
#     else:
#         j += 1
#
# print(max_take)