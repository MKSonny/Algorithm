cnt = 0
def merge(a, left, mid, right):
    i = left
    j = mid + 1
    k = left
    global cnt
    cnt += 1
    sorted = [0] * len(a)
    # print(cnt)
    # print('before sorted: ', a)
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            sorted[k] = a[i]
            i, k = i + 1, k + 1
        else:
            sorted[k] = a[j]
            j, k = j + 1, k + 1
    if i > mid:
        sorted[k : k + right - j + 1] = a[j : right + 1]
    else:
        sorted[k : k + mid - i + 1] = a[i: mid + 1]

    a[left : right + 1] = sorted[left: right + 1]
    print('sorted', sorted)
    # 아래처럼 하면 이전 sorting 된 값들을 기억하지 못하고
    # merge 함수가 호출 될 때마다 새로운 sorted 배열의 값을 가리키게 된다.
    # a = sorted
    print('a', a)

def merge_sort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        # print('a', a)

        merge(a, left, mid, right)

a = [5, 8, 1, 3, 2, 6, 4, 7, 7]
print(a)
merge_sort(a, 0, len(a) - 1)
print(a)