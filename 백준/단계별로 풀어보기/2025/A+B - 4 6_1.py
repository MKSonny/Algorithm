import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '':
        break

    a, b = map(int, s.split())
    print(a + b)