# w: 배낭의 수용 가능한 최대 무게 (배낭의 용량).
# wt: 각 아이템의 무게가 저장된 배열.
# val: 각 아이템의 가치가 저장된 배열.
# n: 사용 가능한 아이템의 수.

def knapsack_bf(w, wt, val, n):
    if n == 0 or w == 0:
        return 0

    if (wt[n - 1] > w):
        return knapsack_bf(w, wt, val, n - 1)
    else:
        valWith = val[n - 1] + knapsack_bf(w - wt[n - 1], wt, val, n - 1)
        valWithout = knapsack_bf(w, wt, val, n - 1)
        return max(valWith, valWithout)

w = 5
wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
n = 4

result = knapsack_bf(5, wt, val, 4)
print("최대 가치:", result)
