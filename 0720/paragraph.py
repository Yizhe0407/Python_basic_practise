# 2023/07/20
import string

paragraph = '''Silicon Stone Education is an unbiased organization, concentrated on briding the 
gap between academic and the working world in order to benefit society as a whole.
We have carefully crafted our online certifiction system and test content databases.
The content for each topic is created by experts and is all carefully designed with a
comprehensive knowledge to greatly benefit all candidates who participate.'''

# 去除标点符号并将字符串转换为单词列表
translator = str.maketrans('', '', string.punctuation)
paragraph_no_punctuations = paragraph.translate(translator)
word_list = paragraph_no_punctuations.lower().split()

# 去除重复单词并转换回列表
word_list_no_duplicates = list(set(word_list))

# 按每行六个元素输出
for i in range(0, len(word_list_no_duplicates), 6):
    line = word_list_no_duplicates[i:i+6]
    print(" ".join(line))
   