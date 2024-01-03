n, m = map(int, input().split())
l = []

for _ in range(n):
    l.append(int(input()))

def binary_search(l, lt, rt, key):
    result = 0

    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 0

        for k in l:
            cnt += k // mid

        if cnt >= key:
            lt = mid + 1
            result = mid
        else:
            rt = mid - 1

    return result

print(binary_search(l, 1, max(l), m))