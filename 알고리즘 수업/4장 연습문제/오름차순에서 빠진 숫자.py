def find_missing_number(arr):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        # 중간 인덱스(mid)의 값과 mid+1이 같으면 빠진 숫자는 mid+2 이후에 있다.
        if arr[mid] == mid + 1:
            left = mid + 1
        # 중간 인덱스(mid)의 값과 mid+1이 다르면 빠진 숫자는 mid 이전에 있다.
        else:
            right = mid

    return left + 1

def binary_search(a, left, right):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == mid + 1:
            return binary_search(a, mid + 1, right)
        else:
            return binary_search(a, left, mid - 1)
    return left + 1

data = [1, 2, 3, 5, 6]
print(binary_search(data, 0, len(data) - 1))