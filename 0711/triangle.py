# 2023/07/11
len1, len2, len3 = eval(input("請輸入3邊長："))
if (len1 + len2) > len3:
    if (len2 + len3) > len1:
         if (len1 + len3) > len2:
              print(f"三角形周長是：{len1 + len2 + len3}")
         else:
              print("這不是三角形的邊長")
    else:
        print("這不是三角形的邊長")
else:
        print("這不是三角形的邊長")

# 精簡版
# len1, len2, len3 = eval(input("請輸入3邊長："))

# if (len1 + len2) > len3 and (len2 + len3) > len1 and (len1 + len3) > len2:
#     print(f"三角形周長是：{len1 + len2 + len3}")
# else:
#     print("這不是三角形的邊長")
        