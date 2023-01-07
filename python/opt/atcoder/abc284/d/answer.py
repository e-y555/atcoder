for _ in range(int(input())):
    n = int(input())
    i = 2
    while i*i*i < n and n % i != 0:
        i += 1
    if n % (i * i) == 0:
        print(i, n // (i*i))
    else:
        print(int((n//i)**0.5), i)