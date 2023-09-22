from queue import Queue
import random

BUCKETS = 10
DIGITS = 4
data = []

def radix_sort(A):
    queue = []
    for i in range(BUCKETS):
        queue.append(Queue())
    n = len(A)
    factor = 1
    print('fist test', A)
    for d in range(DIGITS):
        for i in range(n):
            # 10으로 나누면 가장 마지막 자릿수가 나온다.
            queue[(A[i] // factor) % BUCKETS].put(A[i])
            print('test', (A[i] // factor) % BUCKETS)
        j = 0
        for b in range(BUCKETS):
            while not queue[b].empty():
                A[j] = queue[b].get()
                j += 1
        # d를 DIGITS만큼 해주는 이유는 아래를 4번 호출하여
        # 모든 자릿수에 대해서 연산이 가능하도록 설정
        factor *= BUCKETS
        print("step", d + 1, A)

for i in range(10):
    data.append(random.randint(1, 9999))
radix_sort(data)
print("Radix: ", data)