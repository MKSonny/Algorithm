w = 5
wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
n = 4

def knapsack_dp(w, wt, val, n):
    A = [[0 for x in range(w + 1)] for x in range(n + 1)]
    print('*'*100)
    print(A)
    print('*'*100)

    for i in range(1, n + 1):
        for w in range(1, w + 1):
            # 배낭에 넣을 물건이 더 크면
            if wt[i - 1] > w:
                print(i)
                print(w)
                A[i][w] = A[i - 1][w]
                print(A)
            else:
                # current_item_value = val[i - 1]  현재 아이템의 가치
                # previous_best_value = A[i - 1][w - wt[i - 1]] // 이전 단계의 최적 가치
                # 중요) 이전 단계의 최적 가치란
                # i - 1은 이전에 계산했던 row 중에서 내가 현재 물건을 추가시킨다면 남는 공간들 중
                # 최댓값을 선택하는 것과 동일하다.
                # result = current_item_value + previous_best_value

                valWith = val[i - 1] + A[i - 1][w - wt[i - 1]]
                valWithout = A[i - 1][w]
                A[i][w] = max(valWith, valWithout)
        print()
    return A[n][w]

max = knapsack_dp(w, wt, val, n)
print(max)