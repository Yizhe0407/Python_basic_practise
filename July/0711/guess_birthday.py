# 2023/07/11
day = 0
print("猜生日日期遊戲,請回答下列5個問題,這個程式即可列出你的生日")
qus = "有沒有看到自己的生日日期：\n"
print(qus + "1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31")
ans = input("輸入y或Y代表有,其它代表無：")
if ans == 'y' or ans == 'Y':
    day += 1
print(qus + "2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31")
ans = input("輸入y或Y代表有,其它代表無：")
if ans == 'y' or ans == 'Y':
    day += 2
print(qus + "4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31")
ans = input("輸入y或Y代表有,其它代表無：")
if ans == 'y' or ans == 'Y':
    day += 4
print(qus + "8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31")
ans = input("輸入y或Y代表有,其它代表無：")
if ans == 'y' or ans == 'Y':
    day += 8
print(qus + "16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31")
ans = input("輸入y或Y代表有,其它代表無：")
if ans == 'y' or ans == 'Y':
    day += 16
print(f"你的生日日期是：{day}")

# 精簡版
day = 0
questions = [
    "1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31",
    "2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31",
    "4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31",
    "8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31",
    "16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31"
]

for i, question in enumerate(questions):
    qus = f"有沒有看到自己的生日日期 ({question})："
    ans = input(qus + " 輸入y或Y代表有，其它代表無：")
    if ans == 'y' or ans == 'Y':
        day += 2**i

print(f"你的生日日期是：{day}")
