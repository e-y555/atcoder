n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

for i in range(q):
    flag = False
    for j in range(n):
        if m[i] <= a[j]:
            continue
        sub = m[i] - a[j]
        for k in range(j + 1, n):
            if sub == a[k]:
                flag = True
                break
    if flag:
        print('Yes')
    else:
        print('No')