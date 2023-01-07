T = int(input())

for i in range(T):
    a = int(input())
    b = list(map(int, input().split()))
    ans = 0
    for x in b:
        if x % 2 != 0:
            ans += 1
    print(ans)