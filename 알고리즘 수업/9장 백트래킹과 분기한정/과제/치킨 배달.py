n, m = map(int, input().split())

city = list(list(map(int, input().split())) for _ in range(n))

house = []
chicken = []

for i in range(n):
    for j in range(n):
        # 집의 위치 좌표
        if city[i][j] == 1:
            house.append((i, j))
        # 치킨집의 위치 좌표
        if city[i][j] == 2:
            chicken.append((i, j))

# print(house)
# print(chicken)

INF = 9999

def from_house_distance(house, chicken):
    total = 0

    dist = [INF] * len(house)

    for chicken_distance in chicken:
        c_y = chicken_distance[0]
        c_x = chicken_distance[1]
        for i in range(len(house)):
            h_y = house[i][0]
            h_x = house[i][1]
            distance = abs(h_y - c_y) + abs(h_x - c_x)
            if distance < dist[i]:
                dist[i] = distance

    # print('distacne', dist)
    # print('distacne sum', sum(dist))
    return sum(dist)


def combination(s, sol, k, level, min_dist):
    if len(sol) == k:
        # 여기서 계산
        temp_min = from_house_distance(house, sol)
        if temp_min < min_dist:
            min_dist = temp_min
        return min_dist

    # if level == len(s):
    #     print(min_dist)

    for i in range(level, len(s)):
        sol.append(s[i])
        min_dist = combination(s, sol, k, i + 1, min_dist)
        sol.pop()

    return min_dist

print(combination(chicken, [], m, 0, INF))