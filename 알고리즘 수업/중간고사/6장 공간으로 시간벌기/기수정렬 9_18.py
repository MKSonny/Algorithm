from queue import Queue
import random

DIGITS = 4
BUCKETS = 10
# m = queue.Queue
# m.empty()

def my_sort(A):
    queues = []
    factor = 1

    for _ in range(BUCKETS):
        queues.append(Queue())

    for d in range(DIGITS):
        j = 0

        for item in A:
            queues[(item // factor) % BUCKETS].put(item)

        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1

        factor *= 10

data = []
for i in range(10):
    data.append(random.randint(1, 9999))

print(data)
my_sort(data)
print(data)