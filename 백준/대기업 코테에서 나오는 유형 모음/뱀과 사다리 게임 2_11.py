import sys

n, m = map(int, sys.stdin.readline().split())

la = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    la.append((a, b))

sn = []
for _ in range(m):
    sn.append(map(int, list(sys.stdin.readline().split())))

# 건너뛸 수 있음
# 무조건 사다리 쪽으로 이동
# 이후 뱀쪽을 밟지 않게 이동
# 가장 가까이 있는 사다리로 이동

la.sort(key=lambda o:-(o[1] - o[0]))

for a, b in la:
    print(a, b)
