import sys

s = list(sys.stdin.readline().rstrip())
target = list(sys.stdin.readline().rstrip())
m = len(target)
st = []

for i in s:
    st.append(i)

    if st[len(st) - m:len(st) + m] == target:
        for _ in range(m):
            st.pop()

if st:
    print(*st, sep='')
else:
    print('FRULA')