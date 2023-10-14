import math


def closest_pair(a):
    min = float('inf')
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = distance(a[i], a[j])
            if min > distance(a[i], a[j]):
                min = d
    return min


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(p))