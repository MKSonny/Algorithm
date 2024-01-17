n = int(input())

def search(s):
    for i in range(len(s)):
        if s[i].lower() != s[len(s) - 1 - i].lower():
            return 'NO'
    return 'YES'

c = []

for i in range(n):
    c.append(input())

for idx, value in enumerate(c):
    t = search(value)
    print("#%d %s" % (idx + 1, t))