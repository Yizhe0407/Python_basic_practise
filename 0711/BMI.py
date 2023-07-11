# 2023/07/11
weight = eval(input("please input weight(Kg):"))
height = eval(input("please input height(CM:)")) / 100
BMI = weight / pow(height, 2)
print(f"{BMI = :4.2f}")
if BMI < 18.5:
    print("過輕")
elif BMI >= 18.5 and BMI < 24:
    print("正常")
elif BMI >= 24 and BMI < 28:
    print("超重")
elif BMI >= 28:
    print("肥胖")