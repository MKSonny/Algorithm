import sys

word = list(sys.stdin.readline().rstrip())

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']

d = {
    'a':-1, 'b':-1, 'c':-1, 'd':-1, 'e':-1,
    'f':-1, 'g':-1, 'h':-1, 'i':-1, 'j':-1,
    'k':-1, 'l':-1, 'm':-1, 'n':-1, 'o':-1,
    'p':-1, 'q':-1, 'r':-1, 's':-1, 't':-1,
    'u':-1, 'v':-1, 'w':-1, 'x':-1, 'y':-1,
    'z':-1
}

for idx, i in enumerate(word):
    if d[i] != -1:
        continue
    d[i] = idx

for i in alpha:
    print(d[i], end=' ')