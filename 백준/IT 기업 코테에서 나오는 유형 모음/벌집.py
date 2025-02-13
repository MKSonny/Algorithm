'''
첫 번째 원은 (1 ~ 7) -> 6개
두 번째 원은 (8 ~ 19) -> 12개
세 번째 원은 (20 ~ 37) -> 18개
네 번째 원은 (38 ~ 61) -> 24개

입력 13: 1 -> 4 -> 13
입력 58: 1 -> 6 -> 17 -> 34 -> 58
1 + 6 + 12 + 18 + 24
'''
import sys

n = int(sys.stdin.readline())
start = 1
cnt = 1

while start < n:
    start += (6 * cnt)
    cnt += 1

print(cnt)