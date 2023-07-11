# 2023/07/11
# 華氏溫度與攝氏溫度轉換
print("溫度轉換選擇")
print("1. 華氏溫度轉攝氏溫度")
print("2. 攝氏溫度轉華氏溫度")

choose = int(input("請輸入選擇: "))

if choose == 1:
    f = float(input("請輸入華氏溫度："))
    c = (f - 32) * 5 / 9
    print(f"華氏{f} 等於 攝氏{c:.1f}")
elif choose == 2:
    c = float(input("請輸入攝氏溫度："))
    f = c * 9 / 5 + 32
    print(f"攝氏{c} 等於 華氏{f:.1f}")
else:
    print("輸入錯誤，程式結束")
