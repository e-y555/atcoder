S = list(input())
T = list(input())

for i in range(1, len(T)):
    if S[i - 1] != T[i - 1]:
        print(i)
        break
else:
    print(len(T))
