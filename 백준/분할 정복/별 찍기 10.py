import sys
def pattern(n):
  if n==1:
    return ['*']

  # n = 9
  # stars = draw_stars(3)
  # n = 3
  # stars = draw_stars(1)
  # n = 1
  # stars = return ['*']
  # => 하나의 패턴 출력하지 않고
  # return L 하나의 패턴이 들어있는 리스트를 반환
  '''
  stars = return L
  그러면 n = 9일 경우
  stars = 3일 때의 패턴이 된다.
  그리고 다시 반복문으로 들어가서
  for star in stars니까 하나의 for문당 3번 반복
  첫 반복문에서 star = '***' * 3 이걸 append
  다음에는 '* *' * 3을 append, 마지막으로 '***' * 3을 append
  다음 for문에서는
  '***' + ' ' * n = 9니까 3 + star 이걸 패턴에 따라 반복
  '''
  Stars=pattern(n//3)
  L=[]

  for star in Stars:
    L.append(star*3)
  for star in Stars:
    L.append(star+' '*(n//3)+star)
  for star in Stars:
    L.append(star*3)

  return L


n = int(sys.stdin.readline())
for i in pattern(n):
  print(i)