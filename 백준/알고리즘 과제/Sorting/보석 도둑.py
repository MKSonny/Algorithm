n, m = map(int, input().split())

dia = []
bag = []

for _ in range(n):
    dia.append(list(map(int, input().split())))

for _ in range(m):
    bag.append(int(input()))

max_val = 0

# 0, 1 1, 1 , 0, 1

# 먼저 다이아몬드의 가치를 높은 순으로 배치한다.
# 그리고 가방을 큰 무게 순으로 배치한다.
# 다이아몬드의 가치에 해당하는 무게와 가방을 비교하고 작으면 가방에 다이아몬드를 pop(0)한다.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0][1]  # 기준 값으로 리스트의 첫 번째 항목의 두 번째 요소를 선택
        less = [x for x in arr[1:] if x[1] >= pivot]
        greater = [x for x in arr[1:] if x[1] < pivot]
        return quick_sort(greater) + [arr[0]] + quick_sort(less)

for i in range(n - 1):
    max_val = i
    for j in range(i + 1, n):
        if dia[j][1] > dia[max_val][1]:
            max_val = j

    dia[i], dia[max_val] = dia[max_val], dia[i]

for i in range(m - 1):
    max_val = i
    for j in range(i + 1, m):
        if bag[j] > bag[max_val]:
            max_val = j

    bag[i], bag[max_val] = bag[max_val], bag[i]

max_take = 0

# print(dia)
# print(bag)
i = 0
j = 0

while True:
    if len(bag) == 0:
        break

    if bag[0] >= dia[j][0]:
        max_take += dia.pop(0)[1]
        bag.pop()
    else:
        j += 1

print(max_take)