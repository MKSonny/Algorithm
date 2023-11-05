def knapSack_mem(W, wt, val, n):
    if A[n][W] == None :
        if n == 0 or W == 0 :
            A[n][W] = 0
        elif (wt[n-1] > W):
            A[n][W] = knapSack_mem(W, wt, val, n-1)
        else:
            valWithout = knapSack_mem(W, wt, val, n-1)
            valWith = val[n-1] + knapSack_mem(W-wt[n-1], wt, val, n-1)
            A[n][W] = max(valWith, valWithout)

    return A[n][W]
