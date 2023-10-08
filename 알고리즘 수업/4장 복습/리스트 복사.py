sort_a = [1, 5, 8, 0, 0, 0, 0, 0]
sort_b = [0, 0, 0, 2, 3, 0, 0, 0]
c = [5, 8, 1, 2, 6, 4, 7, 7]
left = 0
right = len(c) - 1

c[left: right + 1] = sort_a[left: right + 1]
c[left: right + 1] = sort_b[left: right + 1]
print(c)