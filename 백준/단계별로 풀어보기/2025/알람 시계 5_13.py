import sys

hour, minute = map(int, sys.stdin.readline().split())
minute -= 45

if minute < 0:
    minute += 60
    hour -= 1

if hour < 0:
    hour = 23

print(hour, minute)