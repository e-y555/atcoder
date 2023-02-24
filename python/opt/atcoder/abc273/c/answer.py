from collections import Counter
N = int(input())
A = list(map(int, input().split()))
count = Counter(A)
S = sorted(list(set(A)))[::-1]
for n in S:
    print(count[n])
for i in range(N-len(S)):
    print(0)

