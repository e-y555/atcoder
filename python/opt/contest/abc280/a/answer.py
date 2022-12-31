H, W = map(int, input().split())

ans = 0
for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == '#':
            ans += 1
print(ans)