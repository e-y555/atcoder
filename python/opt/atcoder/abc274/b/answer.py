H, W = map(int, input().split())
ans = [0 for _ in range(W)]

for i in range(H):
    c = input()
    for j in range(W):
        if c[j] == '#':
            ans[j] += 1
print(*ans)