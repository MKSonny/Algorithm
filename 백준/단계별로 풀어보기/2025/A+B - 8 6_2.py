import sys

n = int(sys.stdin.readline())

idx = 1

while True:
    s = sys.stdin.readline().rstrip()
    if not s:
        break

    a, b = map(int, s.split())

    print("Case #" + str(idx) + ": " + str(a) + ' + ' + str(b) + ' = ' + str(a + b))
    idx += 1