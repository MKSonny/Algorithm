a = [6, 2, 5, 3]
b = [5, 2, 7, 3, 8, 9]
for i in range(a[1] - 1, a[2] - 2):
    least = i
    for j in range(i + 1, a[2] - 1):
        if b[least] > b[j]:
            least = j
    b[least], b[i] = b[i], b[least]

print(b)
print(b[ (a[1] - 1) + (a[3] - 1)])