# 2023/07/29
# method 1
import calendar
year = eval(input('請輸入年份：'))
month = eval(input('請輸入月份：'))
print('-' * 20)
print(calendar.month(year, month))


# method 2
import calendar

def get_valid_input(prompt):
    while True:
        try:
            value = eval(input(prompt))
            return value
        except:
            print("请输入有效的整数值！")

year = get_valid_input('请输入年份：')
month = get_valid_input('请输入月份：')

print('-' * 20)
print(calendar.month(year, month))
