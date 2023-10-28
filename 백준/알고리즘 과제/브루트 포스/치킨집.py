n, m = map(int, input().split())

city = list(list(map(int, input().split())) for _ in range(n))

chicken = []
house = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))

print(house)
print(chicken)

# 1이면 무조건 하나의 리스트에서 합의 최솟값을 찾아야 한다.
# 2면.. 일단 리스트를 통채로 비교할 수는 없다. 원소단위로 비교해야한다.
# 4번째 원소랑 비교했는데 내가 아니다? 그럼 cnt += 1
# 그리고 4번째부터는 나의 기준이 그 최소 원소가 있는 리스트가 된다.

# 아래는 하나씩만 선택했을 경우의 반복문
for i, chicken_xy in enumerate(chicken):
    least = 10000000
    calc = 0
    chicken[i] = []
    for value in house:
        calc = abs(value[0] - chicken_xy[0]) + abs(value[1] - chicken_xy[1])
        chicken[i].append(calc)

print(chicken)

# 일단 두개를 무조건 무식하게 선택?
# 그럼 한개는 어떻게..



"""
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
"""