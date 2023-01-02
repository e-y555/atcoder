H, W = map(int, input().split())

S = []
T = []

for i in range(H):
    s = input()
    S.append(s)

for i in range(H):
    t = input()
    T.append(t)

S = list(zip(*S))
T = list(zip(*T))

S = sorted(S)
T = sorted(T)

if S == T:
    print('Yes')
else:
    print('No')