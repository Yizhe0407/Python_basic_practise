# 2023/07/22
def isPalindrome(Strings):
    length = len(Strings)
    for i in range(length // 2):
        if Strings[i] != Strings[length - 1 - i]:
            return False
    return True

input_string = input('請輸入字串：')
input_list = list(input_string)

if isPalindrome(input_list):
    print(f'{input_string} 是回文字串')
else:
    print(f'{input_string} 不是回文字串')


#遞迴寫法
def isPalindrome(Strings):
    if len(Strings) <= 1:
        return True
    else:
        return Strings[0] == Strings[-1] and isPalindrome(Strings[1:-1])

input_string = input('請輸入字串：')

if isPalindrome(input_string):
    print(f'{input_string} 是回文字串')
else:
    print(f'{input_string} 不是回文字串')
