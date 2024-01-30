import sys

n, m = map(int, sys.stdin.readline().split())
l = []

for _ in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()

def count(l, distance):
    for i in l:
        if i + distance ==

# l은 dis?가 아니고 lt, rt, mid 자체가 거리가 된다.
def binary_search(l, lt, rt, distance, selected):
    if lt > rt:
        return
    mid = (lt + rt) // 2
    if abs(selected - l[mid]) >= distance:
        # mid를 반환하면 끝나버린다.
        # 자신을 기준으로 좌우를 고려해야 한다.
        # 그리고 거리가 더 작은 것을 선택해야 한다.
        # 마지막 정답이 3이 나올 때까지 여기로 들어오면 안된다.
        # 또한 cnt == 3이 되어야 맞는 답이다.
        distance = max(l[mid] - l[lt], l[rt] - l[mid])
        return distance
    elif cnt > m:
        return binary_search(l, lt, mid - 1, distance)
    else:
        return binary_search(l, mid + 1, rt, distance)

print(dis)
# 1을 기준으로 distance가 8인게 있는 지 검사

binary_search(l, 0, len(l) - 1, max(l) - min(l))
# binary_search(l, min(l), max(l))

