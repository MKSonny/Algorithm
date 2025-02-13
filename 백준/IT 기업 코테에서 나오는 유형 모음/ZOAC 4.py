import math
import sys

h, w, n, m = map(int, sys.stdin.readline().split())

# n이 1이라면 한 사람당 2칸을 잡아야한다.
# 근데 마지막 한 사람은 추가 아래 한 칸에 자리가 없어도 사람은 없으므로
# 반올림 한다.
a = math.ceil(h / (n + 1))
b = math.ceil(w / (m + 1))

print(a * b)