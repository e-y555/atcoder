n, p, q, r, s = map(int,input().split())
a = input().split()
a[r-1:s], a[p-1:q] = a[p-1:q], a[r-1:s]
print(' '.join(a))
