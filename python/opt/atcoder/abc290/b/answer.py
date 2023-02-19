N, K = map(int, input().split())
S = list(input())

ans = []
for i in range(N):
    if S[i] == 'o' and K != 0:
        ans.append('o')
        K -= 1
    else:
        ans.append('x')
print(''.join(ans))