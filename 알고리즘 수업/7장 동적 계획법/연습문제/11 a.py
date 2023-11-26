def knapSack_mem(W, wt, val, n, A):
    if A[n][W] == None :
        if n == 0 or W == 0 :
            A[n][W] = 0
        elif (wt[n-1] > W):
            A[n][W] = knapSack_mem(W, wt, val, n-1, A)
        else:
            valWithout = knapSack_mem(W, wt, val, n-1, A)
            valWith = val[n-1] + knapSack_mem(W-wt[n-1], wt, val, n-1, A)
            A[n][W] = max(valWith, valWithout)

    for i in A:
        print(i)

    return A[n][W]

val = [26, 20, 14, 40, 50]
wt = [3, 2, 1, 4, 5]
W = 6
n = len(val)

A = [[None for _ in range(W + 1)] for _ in range(n + 1)]

knapSack_mem(W, wt, val, n, A)