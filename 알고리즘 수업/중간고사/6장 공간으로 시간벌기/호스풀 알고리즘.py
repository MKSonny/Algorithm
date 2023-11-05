n = 3
visit = [False] * (n+1)
s = []

def dfs():
	if len(s) == n:
		print(*s)
		return

	for i in range(1,n+1):
		if visit[i] == False:
			s.append(i)
			visit[i] = True
			dfs()
			s.pop()
			visit[i] = False

dfs()