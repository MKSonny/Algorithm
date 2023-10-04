import sys

sys.setrecursionlimit(10000)
n = input()
a = list(map(int, input().split()))
# 문제에서
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
save_idx = [-1]

for i in range(1, len(a)):
    if res[-1] < a[i]:
        res.append(a[i])
        save_idx.append(i)
    else:
        # print(res)
        idx = binary_search(res, a[i], 0, len(res) - 1)
        # idx_idx = binary_search(save_idx, i, 0, len(save_idx) - 1)
        # print('save_idx', save_idx)
        # print(res, idx_idx)
        # 중간에 낑겨 들어 가면 틀린답
        # if idx_idx == len(save_idx) - 1:
        # print(res, save_idx)
        if len(res) > 1 and idx != len(res) - 1:
            if save_idx[idx + 1] < i:
                continue
        save_idx[idx] = i
        res[idx] = a[i]
print(len(res))
print(res)
# print(save_idx)