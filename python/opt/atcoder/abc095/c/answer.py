a, b, c, x, y = map(int, input().split())

min_xy = min(x, y)
max_xy = max(x, y)

# cは２枚で1つなので * 2
# abピザを買い、足りない分をa, bそれぞれ買う
ans1 = c * min_xy * 2 + a * (x - min_xy) + b * (y - min_xy)
# abピザを買わない
ans2 = a * x + b * y
# 全てabピザ
ans3 = c * max_xy * 2
# 最小金額を出力
print(min(ans1, ans2, ans3))