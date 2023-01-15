N = int(input())
X = 100000

ans = 0
while(True):
    ans += 1
    if ans == N:
        break
    X += 1

X = list(str(X))
X.insert(1, X[0])
X.insert(5, X[4])
X.append(X[-2])
print(''.join(X))