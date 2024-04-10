import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    # 아래는 세 변의 길이를 모두 합하고 거기에서 가장 긴 길이를 빼면
    # 가장 긴 길이의 변을 제외한 남은 두 변의 길이가 나온다.
    # 만약 두 변의 길이의 합이 가장 긴 길이의 변보다 작을 경우를 검사한다.
    if sum((a, b, c)) - max(a, b, c) <= max(a, b, c):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")