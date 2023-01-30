N = int(input())
H = N // 2 + 1

count = 0
for _ in range(N):
    S = input()
    if S == 'For':
        count += 1
    if count >= H:
        print('Yes')
        break
else:
    print('No')