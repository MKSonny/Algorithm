import sys

a = []

for i in range(9):
    a.append(int(input()))

res = [0] * 7

  # 2(치킨집) 를 리스트에 담아서 사이즈를 알수있다.
  dfs(int inx , int count ){
    for(int i =idx ; i< 2.size ; i++){
        //1. 이리시트에서 인덱스를 빼서  x , y를 알 수 있다.
        // 2. 선택한 경우
            map[] 을 2로 냅둔다.
         //  dfs ( i +1 , count + 1)
            map[] = 0;
    }
}


         10   2

def dfs(l, s):
    if l == 7:
        total = 0
        for item in res:
            total += item
        if total == 100:
            for item in res:
                print(item)
    else:
        for i in range(s, 9):
            res[l] = a[i]
            dfs(l + 1, i + 1)

dfs(0, 0)