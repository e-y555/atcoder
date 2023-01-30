N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())
T = []
for _ in range(M):
    T.append(input())

ans = 0
for i in range(N):
    for j in range(M):
        if S[i][-3:] == T[j]:
            ans += 1
            break
print(ans)