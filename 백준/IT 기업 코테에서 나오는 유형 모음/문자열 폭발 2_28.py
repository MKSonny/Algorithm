import sys
from collections import deque

l = list(sys.stdin.readline().rstrip())
l = deque(l)
word = sys.stdin.readline().rstrip()

# print(l)
# print(word)

current = []
temp_word = ''
cnt = 0
while l:
    c = l.popleft()
    temp_word += c
    current.append(c)

    if word in temp_word:
        for _ in range(len(word)):
            current.pop()


if len(current) == 0:
    print('FRULA')
else:
    print(current)
'''
mirkovC4nizCC44
mirkovC4
'''