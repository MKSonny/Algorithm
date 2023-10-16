def merge(a, left, mid, right):
    i = left
    j = mid + 1
    tmp = [0] * len(a)

    while i <= mid and j <= right:
        if a[i] <= a[j]:
            # 같은 경우 i 즉 왼쪽 배열에 있는 것을 먼저
            # tmp에 추가했기 때문에 안정 정렬이 된다.
            tmp[k] = a[i]
            if tmp