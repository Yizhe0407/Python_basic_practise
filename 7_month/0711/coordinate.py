# 2023/07/11
# 計算點座標距離圓中心的長度是否小於半徑
r = 20
x, y = eval(input("請輸入座標："))
length = (((x - 0) ** 2) + ((y - 0) ** 2)) ** 0.5
print(f"點座標 {x}, {y} 在圓內部" if length < r else f"點座標 {x}, {y} 不在圓內部")


if length > r:
    print(f"點座標 {x}, {y} 不在圓內部")
else:
    print(f"點座標 {x}, {y} 在圓內部")
