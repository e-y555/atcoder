N, Q = map(int, input().split())

follows = set()
for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        follows.add((A, B))
    elif T == 2:
        follows.discard((A, B))
    else:
        print('Yes' if (A, B) in follows and (B, A) in follows else 'No')
