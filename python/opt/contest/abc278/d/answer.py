N = int(input())
A = [0] + list(map(int,input().split()))
Q = int(input())

c = 0
Changed = list(range(1,N+1))

for q in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        c = query[1]
        while 0 < len(Changed):
            i = Changed.pop()
            A[i] = 0
    elif query[0] == 2:
        i, x = query[1], query[2]
        A[i] += x
        Changed.append(i)
    elif query[0] == 3:
        i = query[1]
        print(c + A[i])