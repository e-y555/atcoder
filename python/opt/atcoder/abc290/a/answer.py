N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    if i+1 in B:
        ans += A[i]
print(ans)