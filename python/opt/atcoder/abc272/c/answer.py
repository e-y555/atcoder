N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = {'odd': 0, 'even': 0}
even_count = 0
odd_count = 0
for x in reversed(A):
    if x % 2 == 0 and even_count < 2:
        ans['even'] += x
        even_count += 1
    if x % 2 != 0 and odd_count < 2:
        ans['odd'] += x
        odd_count += 1
    if even_count == 2 and odd_count == 2:
        break
if even_count == 2 and odd_count == 2:
    print(max(ans['even'], ans['odd']))
elif even_count == 2 and odd_count < 2:
    print(ans['even'])
elif even_count < 2 and odd_count == 2:
    print(ans['odd'])
else:
    print(-1)