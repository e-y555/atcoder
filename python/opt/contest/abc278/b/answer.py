h, m = map(int, input().split())

while(True):
    h = str(h).zfill(2)
    m = str(m).zfill(2)
    hh = h[0] + m[0]
    mm = h[1] + m[1]
    hh = int(hh)
    mm = int(mm)

    if hh >= 0 and hh <= 23 and mm >= 0 and mm <= 59:
        print(h, m)
        break
    h = int(h)
    m = int(m)
    if m == 59:
        m = 0
        if h == 23:
            h = 0
        else:
            h += 1
    else:
        m += 1


