n = int(input())
list = []
true_list = []
for i in range(n):
    str = input("입력>>> ")
    list.append(str)

def search(A):
    n = len(A)
    for i in range(n):
        p = len(A[i])
        pattern = A[i]
        k = p - 1
        for j in range(p):
            if pattern[j] == pattern[k]:
                if k <= j:
                    true_list.append('true')
                    break
                k -= 1
            else:
                true_list.append('false')
                break
    return -1

search(list)
print(true_list)