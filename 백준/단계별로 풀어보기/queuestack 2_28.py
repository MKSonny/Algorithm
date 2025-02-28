import sys
from collections import deque

n = int(sys.stdin.readline())
info = list(map(int, sys.stdin.readline().split()))

data = list(map(int, sys.stdin.readline().split()))

q = deque()

m = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
# for문을 겹칠 수 없다.
for i in range(n):
    if info[i] == 0:
        q.append(data[i])

for i in t:
    q.appendleft(i)
    print(q.pop(), end=' ')


'''
큐면 새로운 값을 추가, 자기 자신을 뻄
스택이면 새로운 값을 뺴고, 자기 자신을 지킴
1은 건너뛴다. 0은 흡수된다.
0이 있는 곳만 덱처럼

큐, 스택, 스택, 큐
[1], [2], [3], [4]
2 입력
[1, 2], [2], [3], [4]
1 get -> 다음 자료구조로 넘김
[2], [2, 1], [3], [4]
2번째 자료구조는 stack이므로 1이 pop 된다.
1을 다음 자료구조로 넘김
[2], [2], [3, 1], [4]
3번째 자료구조도 stack이므로 1이 pop 된다.
[2], [2], [3], [4, 1]
마지막 4번째 자료구조는 queue이므로 4가 get 된다.
최종: [2], [2], [3], [1]
첫 번째 출력은 4가 된다.
'''