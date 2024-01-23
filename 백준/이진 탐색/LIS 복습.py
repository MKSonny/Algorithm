n = int(input())
l = list(map(int, input().split()))

h = [l[0]]

def binary_search(A, key, low, high):
    if low > high:
        return low
    mid = (low + high) // 2
#ab
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return binary_search(A, key, low, mid - 1)
    else:
        return binary_search(A, key, mid + 1, high)

for i in range(1, len(l)):
    if h[-1] < l[i]:
        h.append(l[i])
    else:
        h[binary_search(h, l[i], 0, len(h) - 1)] = l[i]

print(len(h))