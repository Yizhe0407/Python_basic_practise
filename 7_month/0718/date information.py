# 2023/07/18
days = {
    'monday': '星期一',
    'tuesday': '星期二',
    'wednesday': '星期三',
    'thursday': '星期四',
    'friday': '星期五',
    'saturday': '星期六',
    'sunday': '星期日'
}

day = input("請輸入星期幾的英文：").lower()
print(days.get(day, "輸入錯誤"))
