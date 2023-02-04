N, K = map(int, input().split())
S = []
for i in range(K):
    S.append(input())
T = sorted(S)
for i in range(K):
    print(T[i])