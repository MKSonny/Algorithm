# 7 4 9 6 3 8 7 5
string = input("숫자 8개 입력>>>")
data = list(map(int, string.split(' ')))

n = len(data)

def selection_sort(data):
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if data[least] > data[j]:
                least = j
        data[least], data[i] = data[i], data[least]
        print(data)

selection_sort(data)
print(data)