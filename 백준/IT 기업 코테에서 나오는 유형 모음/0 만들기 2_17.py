import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))

def dfs(t, li, level, calc, total, st):
    print(st)
    if total == 0 and level == t:
        # print(st)
        return
    if level == t:
        return


    if calc == '+':
        total += li[level]
    elif calc == '-':
        total -= li[level]
    else:
        total += int(str(li[level - 1])+ str(li[level])) - li[level - 1]

    # 1 - 2 -> total: -1
    # 1 - 2 3 -> level: 2 -> 이전에 level 1까지 함 -> total: -1
    # -> total을 -22로 변경시켜야 됨
    # -> -1 - 21 하면 됨
    # -> 2의 부등호가 -인지 +인지 알아내야 함
    # 1 - 23 -> total: -22
    # 1 -> 1

    if calc == '':
        st = st[:level] + str(int(str(li[level - 1])+ str(li[level]))) + st[level + 1:]
        # st +=
    else:
        st += calc + str(li[level])

    dfs(t, li, level + 1, '+', total, st)
    dfs(t, li, level + 1, '-', total, st)
    dfs(t, li, level + 1, '', total, st)

for t in li:
    test = [i for i in range(1, t + 1)]
    dfs(t, test, 1, '+', 1, '1')
    dfs(t, test, 1, '-', 1, '1')
