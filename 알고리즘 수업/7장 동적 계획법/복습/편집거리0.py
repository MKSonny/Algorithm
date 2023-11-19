S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)

print(m, n)

# 처음 mem은 모두 None으로 초기화 되어 있다.
# 여기서 mem은 무엇을 저장?
mem = [[None for _ in range(n)] for _ in range(m)]

def edit_distance_mem(S, T, m, n, mem):
    if m == 0:
        return n
    if n == 0:
        return m