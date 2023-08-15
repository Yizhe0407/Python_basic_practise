# 2023/07/29
# method 1
import keyword

while True:
    word = input('輸入字串：')
    if word.lower() == 'q':
        break

    is_keyword = keyword.iskeyword(word)
    print(f'{word} {"是" if is_keyword else "不是"}關鍵字')


# method 2
while (True):
    word = input('輸入字串：')
    if word == 'q' or word == 'Q':
        print(f'{word} 不是關鍵字')
        break
    if keyword.iskeyword(word):
        print(f'{word} 是關鍵字')
    else:
        print(f'{word} 不是關鍵字')