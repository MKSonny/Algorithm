S = "tuesday"
T = "thursday"
m = len(S)
n = len(T)

print(m, n)

# Create a memoization table and initialize it with zeros
mem = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

def edit_distance_tab(S, T, m, n, mem):
    # Initialize the memoization table with base cases
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                mem[i][j] = j  # Base case: if S is empty, insert all characters of T
            elif j == 0:
                mem[i][j] = i  # Base case: if T is empty, delete all characters of S
            elif S[i - 1] == T[j - 1]:
                mem[i][j] = mem[i - 1][j - 1]  # Characters match, no operation needed
            else:
                mem[i][j] = min(mem[i - 1][j - 1], mem[i][j - 1], mem[i - 1][j]) + 1  # Take the minimum of three operations: replace, insert, delete

    return mem[m][n]  # The result is stored in the bottom-right cell of the table

print(edit_distance_tab(S, T, m, n, mem))

for row in mem:
    print(row)
