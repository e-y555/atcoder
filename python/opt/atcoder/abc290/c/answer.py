N, K = map(int,input().split())
A = set(map(int, input().split()))

for i in range(K):
    if i in A:
        continue
    else:
        print(i)
        break
else:
    print(K)
