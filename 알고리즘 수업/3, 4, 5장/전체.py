'''
3. 억지기법과 완전 탐색
    1. 선택 정렬
    2. 순차 탐색
    3. 문자열 매칭
    4. 최근접 쌍의 거리
    5. 완전 탐색
    6. 그래프 탐색 (DFS, BFS)
'''



'''
4. 축소 정복 기법 -> 모든 경우의 수(상향식, 하향식)
    1. 삽입 정렬
    2. 위상 정렬
    3. 이진 탐색
    4. 거듭제곱 문제
    5. k번째 작은 수 찾기
5. 분할 정복 기법
    1. 병합 정렬
    2. 퀵 정렬
'''

def quick_select(a, left, right, k):
    pos = partition(a, left, right)
    if pos + 1 == left + k:
        return a[pos]
    elif pos + 1 > left + k:
        return quick_select(a, left, pos - 1, k)
    else:
        return quick_select(a, pos + 1, right, left - (pos + 1) + k)


def partition(a, left, right):
    pivot = a[left]
    low = left + 1
    high = right

    while low <= high:
        while low <= right and a[low] < pivot: low += 1
        while high >= left and a[high] > pivot: high -= 1
        if low < high:
            a[low], a[high] = a[high], a[low]

    a[left], a[high] = a[high], a[left]

    return high

def quick_sort(a, left, right):
    if left < right:
        pos = partition(a, left, right)
        quick_sort(a, left, pos - 1)
        quick_sort(a, pos + 1, right)

def binary_search(a, left, right, key):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            return binary_search(a, mid + 1, right, key)
        else:
            return binary_search(a, left, mid - 1, key)
    return -1

def merge(a, left, mid, right):
    i = left
    j = mid + 1
    k = left
    sorted = [0] * len(a)
    while i <= mid and j <= right:
        # 어떻게 해야 안정성을 만족하는가?
        if a[i] <= a[j]:
            sorted[k] = a[i]
            i, k = i + 1, k + 1
        else:
            sorted[k] = a[j]
            j, k = j + 1, k + 1

    if i > mid:
        sorted[k: k + right - j + 1] = a[j: right + 1]
    else:
        sorted[k: k + mid - i + 1] = a[i: mid + 1]

    a[left: right + 1] = sorted[left: right + 1]


def merge_sort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(a, left, mid)
        merge_sort(a, mid + 1, right)
        merge(a, left, mid, right)

data = [5, 2, 1, 9, 10, 9]
merge_sort(data, 0, len(data) - 1)
print(data)