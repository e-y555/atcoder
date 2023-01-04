import itertools
n, x = map(int, input().split())

s = [1 * i for i in range(1, n + 1)]
result = []
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        for k in range(j + 1, len(s)):
            if s[i] + s[j] + s[k] == x:
                result.append([s[i], s[j], s[k]])
print(len(result))