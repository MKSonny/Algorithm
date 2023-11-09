val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
w = 18
n = len(val)

def knapSack_bf(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if wt[n - 1] > W:
        return knapSack_bf(W, wt, val, n - 1)
    else:
        valWithout = knapSack_bf(W, wt, val, n - 1)
        valWith = val[n - 1] + knapSack_bf(W - wt[n - 1], wt, val, n - 1)
        return max(valWith, valWithout)

print(knapSack_bf(w, wt, val, n))