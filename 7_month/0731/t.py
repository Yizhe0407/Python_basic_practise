# 2023/07/31
def division():
    try:
        num1 = int(input('請輸入第一個數字：'))
        num2 = int(input('請輸入第二個數字：'))
        return num1 / num2
    except ZeroDivisionError:
        print("除數不可為0")
    except ValueError:
        print("除法資料型態不符")


print(division())
