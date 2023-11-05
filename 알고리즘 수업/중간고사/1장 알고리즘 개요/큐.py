import sys

n = int(input())
l = []

for _ in range(n):
        a = input().split()
        o = a[0]
        if o == "push":
            l.append(int(a[1]))
        elif o == "pop":
            if len(l) == 0:
                print(-1)
            else:
                print(l[0])
                del l[0]
        elif o == "size":
            print(len(l))

        elif o == "empty":
            if len(l) == 0:
                print(1)
            else:
                print(0)

        elif o == "front":
            if len(l) == 0:
                print(-1)
            else:
                print(l[0])

        elif o == "back":
            if len(l) == 0:
                print(-1)
            else:
                print(l[-1])