l = list(input())
t = 0
#
for i in l:
    if i.isdigit():
        t = t * 10 + int(i)

def _find(num):
    cnt = 2

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            cnt += 1

    return cnt

print(t)
print(_find(t))