N, A, B = map(int, input().split())
S = input()
ans = 10**20

for i in range(N):
    S = S[1:] + S[0]
    tmp = A * ((i+1)%N)
    for j in range(N//2):
        if S[j] != S[N-(j+1)]:
            tmp += B

    ans = min(ans,tmp)
print(ans)