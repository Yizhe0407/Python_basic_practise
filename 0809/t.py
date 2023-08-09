import re

figures = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
           'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000, }
figures = dict(sorted(figures.items(), key=lambda x: x[1], reverse=True))


def calculate(nums):
    num1, num2 = re.findall(r'[A-Z]+\b', nums)
    if len(num1) == 1:
        sum1 = figures[num1]
    else:
        if num1[0] == num1[1]:
            sum1 = figures[num1[0]] * 2

    # if num2[0] == num2[1]:
    #     sum2 = figures[num2] * 2
    print(sum1)


nums = input()
calculate(nums)
