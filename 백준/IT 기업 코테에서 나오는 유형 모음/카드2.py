import sys
from collections import deque

n = int(sys.stdin.readline())
cards = [i for i in range(1, n + 1)]
cards = deque(cards)
if n <= 2:
    print(n)
else:
    while True:
        cards.popleft() # 맨위의 카드를 버림
        cards.append(cards.popleft())
        if len(cards) == 1:
            print(cards[0])
            break