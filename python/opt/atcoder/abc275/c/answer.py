S = [input() for _ in range(9)]

ans = 0
for Ar in range(9):
    for Ac in range(9):
        for Br in range(Ar, 9):
            for Bc in range(Ac+1, 9):
                if S[Ar][Ac] == '#' and S[Br][Bc]== '#':
                    Cr = Br + (Bc - Ac)
                    Cc = Bc - (Br - Ar)
                    Dr = Cr - (Bc - Cc)
                    Dc = Cc - (Cr - Br)
                    if 0 <= Cr <= 8 and 0 <= Dr <= 8 and 0 <= Cc <= 8 and 0 <= Dc <= 8:
                        if S[Cr][Cc] == '#' and S[Dr][Dc] == '#':
                            ans += 1
print(ans)