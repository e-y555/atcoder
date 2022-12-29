N, T = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
t = T % S

for i in range(N):
    if A[i] > t:
        print(i + 1, t)
        break
    else:
        t -= A[i]
