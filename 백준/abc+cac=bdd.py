for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a * 100 + b * 10 + c) + c* 100+ a * 10 + c == b * 100 + d * 10 + d:
                    print(a, b, c, d)