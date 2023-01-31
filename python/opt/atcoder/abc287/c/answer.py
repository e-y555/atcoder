import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
rode = [[] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    rode[u].append(v)
    rode[v].append(u)

visited = [False for _ in range(N)]
def dfs(now):
    visited[now] = True
    for i in rode[now]:
        if not visited[i]:
            dfs(i)
dfs(0)
if not all(visited):
    print("No")
    exit()

count = 0
for x in rode:
    if len(x) == 1:
        count += 1
    elif len(x) != 2:
        print("No")
        exit()

if count == 2:
    print("Yes")
else:
    print("No")