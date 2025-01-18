l = [4, 3, 2, 1]

for subset in range(1, 1 << 4):
    print(subset, end=": ")
    for idx in range(4):
        if subset & (1 << idx):
            print(l[idx], end=' ')
    print()