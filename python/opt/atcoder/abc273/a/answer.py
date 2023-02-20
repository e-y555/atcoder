N = int(input())

ans = 1
def f(n, ans):
    if n == 0:
        print(ans)
        return
    ans = n * ans
    f(n-1, ans)
f(N, ans)
