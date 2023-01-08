import itertools

N, M = map(int, input().split())
l = [i + 1 for i in range(M)]
c_list = list(itertools.combinations(l, 2))
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 0
while(len(c_list) > 0):
    c = c_list.pop(0)
    result = []
    for i in range(N):
        result.append(max(A[i][c[0] - 1], A[i][c[1] - 1]))
    ans = max(ans, sum(result))

print(ans)
