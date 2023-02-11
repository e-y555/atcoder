from math import gcd
N = int(input())
A = list(map(int, input().split()))

g = 0
for i in range(N):
    g = gcd(g, A[i])

ans = 0
for i in range(N):
    now = A[i] // g
    while now % 2 == 0:
        now //= 2
        ans += 1
    while now % 3 == 0:
        now //= 3
        ans += 1
    if now != 1:
        print(-1)
        exit()
print(ans)
