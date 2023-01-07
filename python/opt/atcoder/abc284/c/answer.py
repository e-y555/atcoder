from collections import defaultdict
N, M = map(int,input().split())
d = defaultdict(list)
vis = [False]*(N+1)

def dfs(n):
  vis[n] = True
  for i in d[n]:
    if vis[i]:
      continue
    dfs(i)

for i in range(M):
  u,v = map(int,input().split())
  d[u].append(v)
  d[v].append(u)

ans = 0
for i in range(1, N+1):
  if not vis[i]:
    ans += 1
  dfs(i)

print(ans)

