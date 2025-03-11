import sys

n = int(sys.stdin.readline())
answer = 0

for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    d = {}

    flag = True

    for idx, i in enumerate(word):
        if i not in d.keys():
            d[i] = idx
        else:
            if d[i] + 1 != idx:
                flag = False
                break
            else:
                d[i] = idx

    if flag:
        answer += 1


print(answer)