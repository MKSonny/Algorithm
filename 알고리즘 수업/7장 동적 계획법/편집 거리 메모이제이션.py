S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)

print(m, n)

# 처음 mem은 모두 None으로 초기화 되어 있다.
# 여기서 mem은 무엇을 저장?
mem = [[None for _ in range(n)] for _ in range(m)]

def edit_distance_mem(S, T, m, n, mem):
    # S에서 T로 바꾸려고 한다.
    # 아무것도 없는 빈문자열에서 T로 만들려면 n번의 삽입 연산이 있어야한다.
    if m == 0:
        return n
    # S에서 빈문자열을 만들려면 m만큼 삭제해야한다.
    if n == 0:
        return m

    if mem[m - 1][n - 1] == None:
        if S[m - 1] == T[n - 1]:
            mem[m - 1][n - 1] = edit_distance_mem(S, T, m - 1, n - 1, mem)
        else:
            '''
            m과 n을 포인터로 생각한다.
            insertion을 할 경우 m은 그대로 n은 하나 증가한다.
            여기서는 문자 끝부터 시작하므로 m은 그래로 n은 하나 감소시킨다.
            그 이유는 m 이전에 T에 있는 하나의 문자를 S에 삽입시킨다 생각하므로
            S는 T와 일치하는게 하나 발생하므로 n은 하나를 줄이지만 아직 m은 해결되지 않았다.
            '''
            mem[m - 1][n - 1] = min(edit_distance_mem(S, T, m - 1, n - 1, mem),
                                    edit_distance_mem(S, T, m, n - 1, mem),
                                    edit_distance_mem(S, T, m - 1, n, mem)) + 1
        print("mem[%d][%d] = " % (m - 1, n - 1), mem[m - 1][n - 1])

    return mem[m - 1][n - 1]

print(edit_distance_mem(S, T, m, n, mem))

for row in mem:
    print(row)