# 2023/07/11
# 一元二次方程
a, b, c = eval(input("請輸入一元二次方程式的係數："))
number = b ** 2 - 4 * a * c
if number > 0:
    ans1 = (-b + number ** 0.5) / (2 * a)
    ans2 = (-b - number ** 0.5) / (2 * a)
    print(f"有2個實數根\nr1 = {ans1:.4f},\tr2 = {ans2:.4f}")
elif number == 0:
    ans = (-b + number ** 0.5) / (2 * a)
    print(f"有1個實數根\nr1 = {ans:.4f}")
else:
    print("沒有實數根")

# 精簡版
a, b, c = eval(input("請輸入一元二次方程式的係數："))
number = b ** 2 - 4 * a * c
root1 = (-b + number ** 0.5) / (2 * a)
root2 = (-b - number ** 0.5) / (2 * a)
if number >= 0:
    print(f"有實數根\nr1 = {root1:.4f}")
    if number > 0:
        print(f"r2 = {root2:.4f}")
else:
    imaginary_part = (-number) ** 0.5 / (2 * a)
    print(f"沒有實數根\n複數根：{root1:.4f} + {imaginary_part:.4f}i, {root1:.4f} - {imaginary_part:.4f}i")
