string_a = list("HELLO WORLD")
string_b = list("GAME OVER")

table = [[0] * len(string_a) for _ in range(len(string_b))]

for i in range(len(string_b)):
    for j in range(len(string_a)):
        if string_b[i] == string_a[j]:
            # print('a')
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])

for row in table:
    print(row)

table[len(string_b) - 1][len(string_a) -1]