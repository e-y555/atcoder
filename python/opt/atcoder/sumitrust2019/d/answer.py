n = int(input())
s = input()

ans = 0
for i in range(1000):
    v = str(i).zfill(3)
    p1 = s.find(v[0])
    if p1 != -1:
        p2 = s.find(v[1], p1 + 1)
        if p2 != -1:
            p3 = s.find(v[2], p2 + 1)
            if p3 != -1:
                ans += 1
print(ans)