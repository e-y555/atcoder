S = input()
T = input()

pre = [False] * (len(S) + 1)
suf = [False] * (len(S) + 1)

def match_or_not(a, b):
    return a == '?' or b=='?' or a ==b


pre[0] = True
for i in range(len(T)):
    if not match_or_not(S[i], T[i]): break
    pre[i+1] = True

S = S[::-1]
T = T[::-1]
suf[0] = True
for i in range(len(T)):
    if not match_or_not(S[i], T[i]): break
    suf[i+1] = True

for i in range(len(T) + 1):
    if pre[i] and suf[len(T) - i]:
        print('Yes')
    else:
        print('No')
