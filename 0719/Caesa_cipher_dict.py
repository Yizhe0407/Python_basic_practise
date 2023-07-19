# 2023/07/19
secret = []
abc = "abcdefghijklmnopqrstuvwxyz"
front = abc[3:]
end = abc[:3]
subtext = front + end
my_dict = {letter: subtext[i] for i, letter in enumerate(abc)}
#my_dict = list(my_dict.items())
print(my_dict)
password = input('原始字串 ')
for pd in my_dict:
    for i in range(len(password)):
        if pd[0] == password[i]:
            secret.append(pd[1])
    
print(secret)

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
    else:
        secret.append(letter)
    
print(secret)
