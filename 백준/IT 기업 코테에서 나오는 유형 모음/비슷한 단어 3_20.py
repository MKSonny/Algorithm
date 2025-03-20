import sys

n = int(sys.stdin.readline())
words = [(sys.stdin.readline().rstrip(), i) for i in range(n)]

prefix = ''
answer_min_idx = float('inf')
words.sort()

for i in range(n - 1):
    # 아예 같은 단어는 제외
    if words[i][0] == words[i + 1][0]:
        continue

    # 단어의 길이
    '''
    abc, abcd
    min(3, 4) = 3
    min_idx = min(2, 0) = 0
    j = 0 -> 1 -> 2
    j += 1
    j = 3
    현재 prefix는 ''
    
    if len(prefix) < j or len(prefix) == j and 0 < answer_min_idx:
        prefix = words[i][0][:j] -> 이전의 j += 1은 이 때의 슬라이싱 때문에 한 것
        answer_min_idx = 0
        
    abcd, abchldp
    maxlen = 4
    min_idx = 0
    
    a, b, c까지 같음 이후 h부터 틀림
    j = 3
    prefix = abc 
    len(prefix) = 3 < 3 조건에 맞지 않음 하지만
    len(prefix) == 3은 맞음 and min_idx(0) < answer_min_idx(0)의 조건에는 맞지 않음
    
    abchldp, abe
    maxlen = 3
    min_idx = 1
    '''
    max_len = min(len(words[i][0]), len(words[i + 1][0]))
    min_idx = min(words[i][1], words[i + 1][1])

    for j in range(max_len):
        # 다르면 바로 종료
        if words[i][0][j] != words[i + 1][0][j]:
            break
        if j == max_len - 1:
            j += 1

    # j는 같은 글자의 수
    if len(prefix) < j or len(prefix) == j and min_idx < answer_min_idx:
        prefix = words[i][0][:j]
        answer_min_idx = min_idx

answer = list()
for word, idx in words:
    if word[:len(prefix)] == prefix:
        answer.append((word, idx))

# idx를 기준으로 정렬
answer.sort(key=lambda x:x[1])

# 상위 2개만 출력한다.
for word in answer[:2]:
    print(word[0])