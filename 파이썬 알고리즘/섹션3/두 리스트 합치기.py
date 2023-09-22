listA = [1, 3, 5]
listB = [2, 3, 6, 7, 9]
temp = []
def add_list(A, B):
    i = 0
    j = 0
    n = len(B)
    m = len(A)
    while i < m:
        if A[i] < B[j]:
            B.insert(j, A[i])
            i += 1
        else:
            j += 1
    print(B)

add_list(listA, listB)