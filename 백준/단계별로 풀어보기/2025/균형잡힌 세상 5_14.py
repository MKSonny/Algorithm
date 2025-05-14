import sys

while True:
    a = sys.stdin.readline().rstrip()
    a = list(a)

    st = []
    flag = True

    for i in a:
        if i == '(' or i == '[':
            st.append(i)
        elif i == ')':
            if len(st) == 0 or st[-1] != '(':
                flag = False
                break
            st.pop()
        elif i == ']':
            if len(st) == 0 or st[-1] != '[':
                flag = False
                break
            st.pop()

    if len(st) > 0:
        flag = False

    if a == ['.']:
        break

    if flag:
        print("yes")
    else:
        print("no")