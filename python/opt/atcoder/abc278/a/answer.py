N, K = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(K):
    A = A[1:N]
    A.append(0)
print(*A)