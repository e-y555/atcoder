H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

V = [0 for _ in range(W)] # 縦の合計管理
Ho = [0 for _ in range(H)] # 横の合計管理

for i in range(H):
    for j in range(W):
        V[j] += A[i][j]
        Ho[i] += A[i][j]

for i in range(H):
    for j in range(W):
        ans = Ho[i] + V[j] - A[i][j]
        print(ans, end=' ')
    print()
