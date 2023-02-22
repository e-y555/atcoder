import math
X, K = map(int, input().split())
for i in range(K+1):
    tmp1 = 10 ** i
    tmp2 = 0.5 * tmp1
    X = math.floor((X + tmp2) / tmp1)
    X = int(X * tmp1)
print(X)
