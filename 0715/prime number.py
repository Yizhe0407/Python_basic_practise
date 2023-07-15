# 2023/07/15
# 計算質數
my_list = []
figure = 2
while len(my_list) <= 19:
    for i in range(2, figure):
        if figure % i == 0:
            break
    else:
        my_list.append(figure)
    figure += 1
print(my_list)
