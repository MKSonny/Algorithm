N, K = map(int, input("두개의 정수 N, K 입력>>").split())
print(N, K)
def common(N, K):
    list = []
    for i in range(1, N + 1):
        if N % i == 0:
            list.append(i)
    print(list)
    return list[K - 1]

print(common(N, K))