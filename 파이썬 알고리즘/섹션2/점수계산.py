n = int(input())
l = list(map(int, input().split()))

prev = 0
score = [0] * n
'''
10 
1 0 1 1 1 0 0 1 1 0
'''
for i in range(n):
    if prev == 1 and l[i] == 1:
        score[i] += score[i - 1] + 1
    elif l[i] == 0:
        score[i] = 0
    else:
        score[i] += 1
    prev = l[i]

print(sum(score))