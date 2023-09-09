
# ! 優化前
while True:
    figure = list(bin(int(input())))
    del (figure[0], figure[0])
    if figure[0] == '0':
        break
    one = 0
    for i in figure:
        if i == '1':
            one += 1
    a = ''.join(figure[i] for i in range(len(figure)))
    print(f'The parity of {a} is {one} (mod 2).')

# ! 優化後
while True:
    decimal_input = int(input())
    if decimal_input == 0:
        break
    binary_str = bin(decimal_input)[2:]  # 转换为二进制字符串，并去掉前缀 '0b'
    parity = binary_str.count('1')
    print(f'The parity of {binary_str} is {parity} (mod 2).')
