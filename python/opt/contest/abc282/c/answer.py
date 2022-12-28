N = int(input())
S = input()

stack = []
flag = False
for i in range(N):
    if S[i] == '"':
        if flag:
            flag = False
        else:
            flag = True
    if S[i] == ',' and not flag:
        stack.append('.')
    else:
        stack.append(S[i])
print(''.join(stack))
