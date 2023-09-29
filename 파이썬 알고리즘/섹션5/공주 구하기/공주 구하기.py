import queue

q1 = queue.Queue()
q2 = queue.Queue()

for i in range(1, 9):
    q1.put(i)
j = 0
while not q1.empty():
    j += 1
    if j % 3 == 0:
        q1.get()
        j += 1
        while not q2.empty():
            q1.put(q2.get())
    q2.put(q1.get())

print(q1.get())