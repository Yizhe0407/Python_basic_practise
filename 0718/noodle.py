# 2023/07/18
noodles = {'牛肉麵': 100, '肉絲麵': 80, '陽春麵': 60, '大滷麵': 90, '麻醬麵': 70}
noodles2 = sorted(noodles.items(), key=lambda x: x[1], reverse=True)
print(f'最貴的是 {noodles2[0][0]} 金額是 {noodles2[0][1]}')
print(f'最便宜的是 {noodles2[-1][0]} 金額是 {noodles2[-1][1]}')
