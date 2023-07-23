# 2023/07/23

def N(cities_number):
    if cities_number == 0 or cities_number == 1:
        return 1
    else:
        return N(cities_number - 1) * cities_number

number = eval(input('請輸入城市的個數：'))
print(f'城市個數 {number},路徑組合數 = {N(number)}')
print(f'需要 {N(number) / (10 * (10 ** 12) * 31556926)} 年才可以獲得結果')
