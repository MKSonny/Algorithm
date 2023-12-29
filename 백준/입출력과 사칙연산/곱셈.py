n = int(input())
m = input()
h = list(m)
# ㅁ
for i in range(len(h) - 1, -1, -1):
    print(int(h[i]) * n)

print(n * int(m))