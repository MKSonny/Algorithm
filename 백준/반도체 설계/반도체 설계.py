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
'''
else:
    # 0, len(res) - 1: 이렇게 하면 절대로
    # binary_search(0, len(res) - 1, arr[i])를 통해 나오는 mid 값은
    # res의 max index 보다 커질 수 없다.
    idx = binary_search(0, len(res) - 1, arr[i])

    print('idx', binary_search(0, len(res) - 1, arr[i]))
    print('res', res)
    res[binary_search(0, len(res) - 1, arr[i])] = arr[i]
'''