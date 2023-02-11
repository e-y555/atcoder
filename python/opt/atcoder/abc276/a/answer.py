S = input()
for i in reversed(range(len(S))):
    if S[i] == 'a':
        print(i + 1)
        break
else:
    print(-1)