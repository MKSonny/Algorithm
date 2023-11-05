def merge_sort_iter(a):
    current_size = 1
    while current_size < len(a) - 1:
        left = 0
        while left < len(a) - 1:
            # 1) 0 + 1 - 1 = 0
            mid = min((left + current_size - 1), len(a) - 1)
            # []는 둘 중 하나 선택 의미
            # 2 * current_size + left - 1 > len(a) - 1 를 만족하면 오른쪽을 선택
            # (2 * 1 + 0 - 1, 4)[2 * 1 + 0 - 1 > 4]
            '''
            current_size: 현재 병합하는 부분 배열의 크기를 나타냅니다. 
            처음에는 1로 시작하고, 그 다음에는 2, 4, 8 등으로 두 배씩 증가하면서 작업을 수행합니다.
            left: 현재 병합하는 부분 배열의 왼쪽 끝 인덱스를 나타냅니다.
            2 * current_size + left - 1: 이 부분은 중간 지점 mid를 계산합니다. 
            이 수식은 현재 병합하려는 부분 배열에서 중간 지점 mid를 나타내며, 
            mid는 부분 배열을 두 개의 부분으로 나눌 때의 중간 지점을 가리킵니다.
            '''
            right = ((2 * current_size + left - 1, len(a) - 1)[2 * current_size + left - 1 > len(a) - 1])
            merge(a, left, mid, right)
            left = left + 2 * current_size
        current_size = 2 * current_size


def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]

    for i in range(0, n2):
        R[i] = a[m + i + 1]

    print(L, R)

    i, j, k = 0, 0, l

    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1

        k += 1

    # 정렬이 먼저 끝난 것을 모두 추가
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

data = [4, 1, 9, 3, 10]
print(data)
merge_sort_iter(data)
print(data)