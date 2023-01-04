S = input()
T = input()
ls = len(S)
lt = len(T)
if ls < lt:
    print('No')
    exit()
elif S == T:
    print('Yes')
    exit()
else:
    flag = False
    for i in range(ls):
        for j in range(lt):
            if S[i] == T[j]:
                if S[i:i+lt] == T:
                    flag = True
if flag:
    print('Yes')
else:
    print('No')