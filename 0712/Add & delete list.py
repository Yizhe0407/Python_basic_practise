original_list = ['Mary', 'Josh', 'Tracy']
print("1.增加名單")
print("2.刪除名單")
choose = int(input(" = "))
if choose == 1:
    name = input("請輸入名字：")
    if name in original_list:
        print("這個名字已經有了")
    else:
        original_list.append(name)
        print(f"新的宴會名單：{original_list}")
else:
    name = input("請輸入名字：")
    if name not in original_list:
        print("名單輸入錯誤")
    else:
        original_list.remove(name)
        print(f"新的宴會名單：{original_list}")
    