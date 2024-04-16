import sys

n = int(sys.stdin.readline())

l = []

left_arm = 0
right_arm = 0
left_leg = 0
right_leg = 0
body = 0

for _ in range(n):
    l.append(list(sys.stdin.readline().rstrip()))

head_y, head_x = -1, -1
heart_y, heart_x = -1, -1

for i in range(n):
    for j in range(n):
        if l[i][j] == '*':
            if head_x == -1:
                head_y, head_x = i, j
            if i == head_y + 1:
                if j < head_x:
                    left_arm += 1
                elif j > head_x:
                    right_arm += 1
                elif j == head_x:
                    heart_y, heart_x = i + 1, j + 1
            if i > head_y + 1:
                if j == head_x:
                    body += 1
                elif j == head_x - 1:
                    left_leg += 1
                elif j == head_x + 1:
                    right_leg += 1

print(heart_y, heart_x)
print(left_arm, right_arm, body, left_leg, right_leg)