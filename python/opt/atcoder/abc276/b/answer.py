N, M = map(int, input().split())
D = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    D[a-1].append(b)
    D[b-1].append(a)
for i in range(N):
    D[i].sort()
    print(len(D[i]), *D[i])