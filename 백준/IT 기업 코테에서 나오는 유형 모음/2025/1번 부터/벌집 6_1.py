import sys

n = int(sys.stdin.readline())

# 1 -> 7(1 + 6) -> 19(7 + 12)
start = 1
i = 1

answer = 1



while True:
    if n == 1:
        break
    start += 6 * i
    answer += 1

    if start >= n:
        break

    i += 1

print(answer)