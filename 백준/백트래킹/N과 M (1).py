def permutaion(n, k, sol, mark):
    if len(sol) == k:
        for key in sol:
            print(key, end=' ')
        print()
        return

    for i in range(1, n + 1):
        if mark[i] == False:
            sol.append(i)
            mark[i] = True
            permutaion(n, k, sol, mark)
            sol.pop()
            mark[i] = False


n, m = map(int, input().split())
mark = [False] * (n + 1)

permutaion(n, m, [], mark)
