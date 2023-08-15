# amount = int(input("請輸入層數：")) + 1
# for i in range(amount):
#     for j in range(1, amount):
#         print(f"{j:d}", end='')
#     amount -= 1
#     print()

# amount = int(input("請輸入層數："))
# for i in range(1, amount + 1):
#     print(''.join(str(j) for j in range(1, i + 1)))

amount = int(input("請輸入層數："))

for i in range(1, amount + 1):
    print(' ' * i + ''.join(str(j) for j in range(amount + 1 - i, 0, -1)))



# rows = 9  # 设定行数
# for i in range(1, rows + 1):
#     print(" " * (rows - i), end='')
#     for j in range(i, 0, -1):
#         print(j, end='')
#     print()
