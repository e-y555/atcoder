S = input()
N = len(S)

stack = []
flag = True
for i in range(N):
    if S[i] == '(':
        continue
    elif S[i] == ')':
        stack = []
    else:
        for j in range(len(stack)):
            if stack[j] == S[i]:
                flag = False
                break
        stack.append(S[i])
if flag: print('Yes')
else: print('No')