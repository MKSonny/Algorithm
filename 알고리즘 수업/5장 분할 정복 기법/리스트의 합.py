def merge(a, left, mid, right):
    return a[left] + a[right]

def merge_sum(a, left, right):
    if left < right:
        mid = (left + right) // 2
        left_sum = merge_sum(a, left, mid)
        right_sum = merge_sum(a, mid + 1, right)
        return left_sum + right_sum
    else:
        return a[left]

def sum_all(n):
    sum = 0
    for i in range(len(n)):
        sum += n[i]
    return sum

data = [101, 2, 3, 4, 5, 30, 100]
idx = merge_sum(data, 0, len(data) - 1)
print(idx)
print(sum_all(data))