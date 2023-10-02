min_ = 99999
a = [4, 2, 6, 3, 1, 5]
def binary_solve(a, left, right):
    global min_
    mid = (left + right)// 2
    if min_ > a[mid]:
        print('a')
        min_ = a[mid]
    else:
        return binary_solve(a, left, mid)

anw = binary_solve(a, 0, len(a) - 1)
print(min_)