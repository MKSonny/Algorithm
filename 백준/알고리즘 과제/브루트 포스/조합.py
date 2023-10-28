a = [1, 2, 3, 4]

def combination(n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            print(a[i], a[j])

func(len(a))