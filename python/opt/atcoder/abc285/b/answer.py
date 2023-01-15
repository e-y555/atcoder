N = int(input())
S = input()

for i in range(1, N):
    ans = 0
    for j in range(N - i):
        if j + i < N:
            if S[j] != S[j + i]:
                ans += 1
            else:
                break
    print(ans)