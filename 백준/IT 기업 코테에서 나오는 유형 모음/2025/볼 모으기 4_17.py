import sys

n = int(sys.stdin.readline())
l = sys.stdin.readline().rstrip()

d = {
    'R': 0, 'B': 0
}

for i in l:
    d[i] += 1

answer = min(d.values())

for color in ['R', 'B']:
    for li in [l, l[::-1]]:
        if li[0] != color:
            continue
        cnt = 1
        for temp_color in li[1:]:
            if temp_color != color:
                break
            cnt += 1

        answer = min(answer, d[color] - cnt)

print(answer)