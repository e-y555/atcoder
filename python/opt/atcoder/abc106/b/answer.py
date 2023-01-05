N = int(input())
ans = 0
for n in range(1, N + 1):
    if n % 2 == 0:
        continue
    arr = []
    for j in range(1, n + 1):
        if j * j > n:
            break
        if n % j != 0:
            continue
        arr.append([j])
        if n // j != j:
            arr.append(n // j)

    if len(arr) == 8:
        ans += 1
print(ans)