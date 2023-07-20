# 2023/07/19
# 加密
secret = []
abc = "abcdefghijklmnopqrstuvwxyz"
front = abc[3:]
end = abc[:3]
subtext = front + end
my_dict = {letter: subtext[i] for i, letter in enumerate(abc)}
#my_dict = list(my_dict.items())
print(my_dict)
password = input('原始字串 ').lower()  # 將輸入轉換為小寫
for letter in password:
    if letter in my_dict:
        secret.append(my_dict[letter])
print('加密字串', end=' ')
for i in secret:
    print(i,end='')


# 解密
abc = "abcdefghijklmnopqrstuvwxyz"
front = abc[3:]
end = abc[:3]
subtext = front + end
my_dict = {letter: subtext[i] for i, letter in enumerate(abc)}

# 解密字典，将加密字母映射回原始字母
decryption_dict = {subtext[i]: letter for i, letter in enumerate(abc)}

# 加密后的字符串
encrypted_string = "sbwkrq"  # 这里替换成你加密得到的字符串

# 解密过程
decrypted_string = ""
for letter in encrypted_string:
    if letter in decryption_dict:
        decrypted_string += decryption_dict[letter]
    else:
        decrypted_string += letter

print("解密后的字符串:", decrypted_string)
