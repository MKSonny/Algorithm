import sys

# 13:5

s = list(sys.stdin.readline().rstrip())
t = list(sys.stdin.readline().rstrip())

s_idx = 0
t_idx = 0

if t == s:
    print(1)
    exit()

flag = False

while t_idx < len(t):
    if s[s_idx] != t[t_idx] or flag:
        if t[t_idx] == 'B':
            if s_idx + 1 < len(s) and s[s_idx + 1] == 'B':
                s.reverse()
            else:
                s.append('B')
                s.reverse()
        else:
            s.append('A')
    t_idx += 1
    if s_idx + 1 >= len(s):
        flag = True
        continue
    s_idx += 1

# print(s)
# print(t)
'''
AB
BAABA
'''
if s == t:
    print('1')
else:
    print('0')