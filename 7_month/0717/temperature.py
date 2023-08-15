# 2023/07/17
highest_temperature = (30, 28, 29, 31, 33, 35, 32)
lowest_temperature = (20, 21, 19, 22, 23, 24, 20)
print(f"過去一周的最高溫度 {max(highest_temperature)}")
print(f"過去一周的最低溫度 {min(lowest_temperature)}")

for high, low in zip(highest_temperature, lowest_temperature):
    temperature = (high + low) / 2
    print(f"{temperature:.1f}", end=' ')
