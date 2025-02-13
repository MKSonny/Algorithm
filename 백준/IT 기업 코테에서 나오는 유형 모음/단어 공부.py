import sys

string = sys.stdin.readline().rstrip().upper()
alpa = [0] * 26

for letter in string:
    alpa[ord(letter) - 65] += 1

max_i = -1
maxx = 1
prev_i = -1

for i in range(26):
    if alpa[i] >= maxx:
        prev_i = max_i
        max_i = i
        maxx = alpa[i]

if len(string) > 1 and alpa[prev_i] == alpa[max_i]:
    print('?')
else:
    print(chr(max_i + 65))