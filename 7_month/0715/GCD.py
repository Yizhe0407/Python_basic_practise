# 2023/07/15
# 求最大公約數
common_Divisor = []

figure1 = int(input("請輸入數值 1 ： "))
figure2 = int(input("請輸入數值 2 ： "))

for i in range(1, max(figure1,figure2)):
    if figure1 % i == 0 and figure2 % i == 0:
        common_Divisor.append(i)

print(f"{figure1} and {figure2} 的最大公約數是： {common_Divisor[-1]}")

# 精簡版
figure1 = int(input("請輸入數值 1 ： "))
figure2 = int(input("請輸入數值 2 ： "))

common_Divisor = [i for i in range(1, max(figure1, figure2)) if figure1 % i == 0 and figure2 % i == 0]

print(f"{figure1} and {figure2} 的最大公約數是： {common_Divisor[-1]}")
