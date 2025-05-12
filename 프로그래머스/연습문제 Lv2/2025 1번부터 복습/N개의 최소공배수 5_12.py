def solution(arr):
    answer = 1

    maxx = 1
    for i in arr:
        maxx *= i

    for i in range(max(arr), maxx + 1):
        flag = True
        for a in arr:
            if i % a != 0:
                flag = False
                break
        if flag:
            return i

    return max(arr)