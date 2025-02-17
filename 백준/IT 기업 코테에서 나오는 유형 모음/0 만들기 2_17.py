import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))


def dfs(t, li, level, st):
    global answer

    if level == t:
        temp = st
        st = st.replace(' ', '')
        # print(st)
        if eval(st) == 0:
            # print(st)
            answer.add(temp)
        return

    dfs(t, li, level + 1, st + '+' + str(li[level]))
    dfs(t, li, level + 1, st + '-' + str(li[level]))
    dfs(t, li, level + 1, st + ' ' + str(li[level]))


for t in li:
    test = [i for i in range(1, t + 1)]
    answer = set()
    dfs(t, test, 1, '1')
    dfs(t, test, 1, '1')
    dfs(t, test, 1, '1')

    answer = list(answer)
    answer.sort()
    for a in answer:
        print(a)
    print()

# print(answer)