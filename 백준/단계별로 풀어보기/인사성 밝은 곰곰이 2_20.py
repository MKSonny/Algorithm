import sys

n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    message = sys.stdin.readline().rstrip()
    if message == 'ENTER':
        members = set()
    else:
        if message not in members:
            members.add(message)
            cnt += 1
        else:
            continue

print(cnt)