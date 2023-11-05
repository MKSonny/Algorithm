from queue import Queue
import random

DIGITS = 4
BUCKETS = 10
data = []

for i in range(10):
    data.append(random.randint(1, 9999))

def radix_sort(A):
    queues = []
    n = len(A)
    factor = 1

    for i in range(BUCKETS):
        queues.append(Queue())

    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i] // factor) % 10].put(A[i])

        j = 0

        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1

        factor *= 10

        print('step', d, A)

radix_sort(data)