# 2023/07/29
# method 1
import string

def encrypt(text, encryDict):          
    '''加密文件'''
    cipher = []
    for i in text:                      
        v = encryDict[i]                
        cipher.append(v)                
    return ''.join(cipher)              

def decrypt(text, encryDict):
    '''解密文件'''
    cipher = []
    for i in text:                      
        v = encryDict[i]              
        cipher.append(v)                
    return ''.join(cipher)              

abc = string.printable[:-5]             # 取消不可列印字元
subText = abc[-3:] + abc[:-3]           # 加密字串
encry_dict = dict(zip(subText, abc))    # 建立加密字典
decry_dict = dict(zip(abc, subText))    # 建立解密字典

msg = 'If the implementation is easy to explain, it may be a good idea.'
ciphertext = encrypt(msg, encry_dict)
decryptedtext = decrypt(ciphertext, decry_dict)
print("原始字串 ", msg)
print("加密字串 ", ciphertext)
print("解密字串 ", decryptedtext)

# method 2
import string

def encrypt(text, encryDict):
    '''加密文件'''
    return ''.join(encryDict.get(c, c) for c in text)

def decrypt(text, encryDict):
    '''解密文件'''
    return ''.join(encryDict.get(c, c) for c in text)

abc = string.ascii_letters + string.digits + string.punctuation + ' '  # 所有可列印的字元
subText = abc[-3:] + abc[:-3]  # 加密字串
encry_dict = dict(zip(abc, subText))  # 建立加密字典
decry_dict = dict(zip(subText, abc))  # 建立解密字典

msg = 'If the implementation is easy to explain, it may be a good idea.'
ciphertext = encrypt(msg, encry_dict)
decryptedtext = decrypt(ciphertext, decry_dict)
print("原始字串 ", msg)
print("加密字串 ", ciphertext)
print("解密字串 ", decryptedtext)
