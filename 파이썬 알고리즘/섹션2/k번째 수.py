n = int(input())

h = []

'''
2
6 2 5 3 
5 2 7 3 8 9 
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
'''

for i in range(n):
    m, s, e, k = map(int, input().split())
    tmp = list(map(int, input().split()))
    tmp = tmp[s - 1:e]
    tmp.sort()
    print("#%d %d" % (i + 1, tmp[k - 1]))