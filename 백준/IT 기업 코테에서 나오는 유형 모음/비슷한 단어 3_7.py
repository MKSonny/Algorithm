import sys

n = int(sys.stdin.readline())
words = []

'''
1113
1112
3125

if in d.keys()
첫 번째 문자
두 분째 문자
'''

for _ in range(n):
    words.append(sys.stdin.readline().rstrip())

words.sort()

d = {}
