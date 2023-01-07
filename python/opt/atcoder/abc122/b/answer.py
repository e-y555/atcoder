S = input()
ans = 0
counter = 0
target = ['A', 'C', 'G', 'T']
for i in range(len(S)):
    if S[i] in target:
        counter += 1
        ans = max(ans, counter)
    else:
        counter = 0
print(ans)