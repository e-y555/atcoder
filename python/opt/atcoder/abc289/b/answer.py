N, M = map(int,input().split())
A = list(map(int,input().split()))
Q = []
ans = []
for i in range(1,N+1):
    if i in A:
        Q.append(i)
    else:
        ans.append(i)
        while Q:
            ans.append(Q.pop())
print(*ans)