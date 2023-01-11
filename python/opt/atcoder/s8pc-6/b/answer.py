import itertools
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
iab = list(itertools.chain.from_iterable(ab))

result = 10 ** 11
for enter in iab:
    for exit in iab:
        t = 0
        for a, b in ab:
            t += abs(a - enter)
            t += (b - a)
            t += abs(b - exit)
        result = min(result, t)
print(result)