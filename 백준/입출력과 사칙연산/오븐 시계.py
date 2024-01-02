hour, minute = map(int, input().split())
n = int(input())

time_passed = minute + n
hour_passed = 0

if time_passed >= 60:
    hour_passed = time_passed // 60
    time_passed -= (60 * hour_passed)

if hour + hour_passed >= 24:
    print(hour + hour_passed - 24, time_passed)
else:
    print(hour + hour_passed, time_passed)