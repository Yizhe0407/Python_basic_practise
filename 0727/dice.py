# 2023/07/28
# method 1
from collections import Counter
import random
my_list = []
amount = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
for i in range(600):
    my_list.append(random.choice([1, 2, 3, 4, 5, 6]))

for i in range(600):
    if 1 == my_list[i]:
        amount['1'] += 1
    elif 2 == my_list[i]:
        amount['2'] += 1
    elif 3 == my_list[i]:
        amount['3'] += 1
    elif 4 == my_list[i]:
        amount['4'] += 1
    elif 5 == my_list[i]:
        amount['5'] += 1
    elif 6 == my_list[i]:
        amount['6'] += 1

for number, quantity in amount.items():
    print(f'{number}：{quantity}')


# method 2
my_list = [random.choice([1, 2, 3, 4, 5, 6]) for _ in range(600)]
amount = dict(sorted(Counter(my_list).items(), key=lambda item: item[0]))

for number, quantity in amount.items():
    print(f'{number}：{quantity}')
