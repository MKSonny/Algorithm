import queue
import sys

sys.stdin = open("in1.txt", "r")
n, k = map(int, input().split())
a = list(map(int, input().split()))

q1 = queue.Queue()

for i in a:
    q1.put(i)

q2 = queue.Queue()

while q1:
    f = q1.get()
    q2.put(f)
    print(f)
    s = q2.get()
    print(s)
    if s > f:
        q1.get()
        while q2:
            q1.put(q2.get())
    else:
        q2.put(f)