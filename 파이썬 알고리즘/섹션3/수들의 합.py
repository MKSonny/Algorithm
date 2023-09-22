# 텍스트 파일 열기
with open('in2.txt', 'r') as file:
    # 파일 내용 읽기
    data = file.read()

# 공백을 기준으로 데이터 분리하여 정수 리스트로 저장
data_list = [int(num) for num in data.split()]

# data_list를 출력하여 확인
print(data_list)

def find_num(A, m):
    tot = A[0]
    n = len(A)
    cnt = 0
    lt = 0
    rt = 1

    while True:
        if tot < m:
            if rt < n:
                tot += A[rt]
                rt += 1
            else:
                break
        elif tot == m:
            tot -= A[lt]
            lt += 1
            cnt += 1
        else:
            tot -= A[lt]
            lt += 1
    return cnt

cnt = find_num(data_list, 100)
print(cnt)