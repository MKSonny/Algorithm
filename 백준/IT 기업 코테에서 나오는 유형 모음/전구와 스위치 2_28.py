import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
make = list(map(int, sys.stdin.readline().split()))

print(l)
print(make)
'''
000과 010 비교 가운데 하나만 차이나면 2번째
101과 000 비교 101이면 맨 왼쪽

011과 000 비교 오른쪽 2개 다르면
만약 차이가 011이라면 맨 오른쪽을

2번째
101
1번째를 누를 경우 011
3번째를 누를 경우 110
011
3번째 -> 2번째는 이전에 이미 눌러서?

000
'''