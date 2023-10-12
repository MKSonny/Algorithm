import queue

def fib(n):
    q = queue.Queue()
    q.put(0)
    q.put(1)
    for i in range(n):
        n1 = q.get()
        n2 = q.get()
        q.put(n2)
        q.put(n1 + n2)

    return q.get()

print(fib(6))