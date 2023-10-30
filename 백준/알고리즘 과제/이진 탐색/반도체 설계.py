n = input()
a = list(map(int, input().split()))
def binary_search(A, key, low, high):
    if low > high:
        return low
    mid = (low + high) // 2
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return binary_search(A, key, low, mid - 1)
    else:
        return binary_search(A, key, mid + 1, high)

res = [a[0]]

for i in range(1, len(a)):
    if res[-1] < a[i]:
        res.append(a[i])
    else:
        # print(res)
        res[binary_search(res, a[i], 0, len(res) - 1)] = a[i]
print(len(res))