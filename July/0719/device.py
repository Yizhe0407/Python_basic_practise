# 2023/07/19
devices = {
    'iWatch手錶': (15000, 0.1),
    'Asus  筆電': (35000, 0.7),
    'iPhone手機': (38000, 0.3),
    'Acer  筆電': (40000, 0.8),
    'Go Pro攝影': (12000, 0.1)
}
devices = sorted(devices.items(), key=lambda x: x[1][1])
print('所有商品依價值排序如下')
print('商品          商品價格   商品重量')
# method 1
for i in range(len(devices)):
    print(f'{devices[i][0]:8s}{devices[i][1][0]:12d}{devices[i][1][1]:11.2f}')

# method 2
for device in devices:
    print(f'{device[0]:8s}{device[1][0]:12d}{device[1][1]:11.2f}')