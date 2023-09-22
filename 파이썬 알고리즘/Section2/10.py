list = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
def calculate(A):
    n = len(list)
    cnt = 0
    score = 0
    for i in range(n):
        if list[i] == 1:
            cnt += 1
            score += cnt
        else:
            cnt = 0
    return score

print(calculate(list))