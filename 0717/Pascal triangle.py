# 2023/07/17
layers = int(input("請輸入層數："))
for n in range(layers):
    print(' '*(layers-n), end='')

    print(' '.join(map(str, str(11**n))))

