import sys

word = list(sys.stdin.readline().rstrip())
st = 0
ed = len(word) - 1

while word[st] == word[ed] and st < len(word) // 2:
    st += 1
    ed -= 1

if st == len(word) // 2: print(1)
else: print(0)