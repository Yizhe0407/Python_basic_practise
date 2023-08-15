# 2023/07/18
# method 1
travels = {
    '張家界': ['湖南省', '天門山', '大峽谷'],
    '九寒溝': ['四川省', '熊貓海', '箭竹海'],
    '黃山': ['安徽省', '天都峰', '蓬萊三島'],
    '武夷山': ['福建省', '天遊峰', '桃源洞'],
    '敦煌': ['甘蕭省', '石窟', '月牙泉']
}
travels = list(travels.items())

for j in range(len(travels)):
    print(f'旅遊地點 = {travels[j][0]}')
    print(f'省份     = {travels[j][1][0]}')
    print(f'景點     = {travels[j][1][1]}, {travels[j][1][2]}')

# method 2
travels = {
    '張家界': ['湖南省', '天門山', '大峽谷'],
    '九寒溝': ['四川省', '熊貓海', '箭竹海'],
    '黃山': ['安徽省', '天都峰', '蓬萊三島'],
    '武夷山': ['福建省', '天遊峰', '桃源洞'],
    '敦煌': ['甘蕭省', '石窟', '月牙泉']
}

for place, info in travels.items():
    print(f'旅遊地點 = {place}')
    print(f'省份     = {info[0]}')
    print(f'景點     = {info[1]}, {info[2]}')