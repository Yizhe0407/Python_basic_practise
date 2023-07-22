# 2023/07/22
# means 1
def computer(figure1, figure2, operator):
    global choose
    if operator == '+':
        print(f'計算結果 = {figure1 + figure2}')
    elif operator == '-':
        print(f'計算結果 = {figure1 - figure2}')
    elif operator == '*':
        print(f'計算結果 = {figure1 * figure2}')
    elif operator == '/':
        print(f'計算結果 = {figure1 / figure2}')
    else:
        print('運算公式輸入錯誤')
    choose = input('是否繼續?(Y or y) = 繼續：')
    return choose

condition = True
while condition:
    num1 = int(input('請輸入第1個數字 = '))
    num2 = int(input('請輸入第2個數字 = '))
    ope = input('請輸入運算子(+, _, *, /)：')
    computer(num1, num2, ope)
    condition = choose in ('Y', 'y')


# means 2
def computer():
    global condition

    figure1 = int(input('請輸入第1個數字 = '))
    figure2 = int(input('請輸入第2個數字 = '))
    operator = input('請輸入運算子(+,_,*,/)：')
    if operator == '+':
        print(f'計算結果 = {figure1 + figure2}')
    elif operator == '-':
        print(f'計算結果 = {figure1 - figure2}')
    elif operator == '*':
        print(f'計算結果 = {figure1 * figure2}')
    elif operator == '/':
        print(f'計算結果 = {figure1 / figure2}')
    else:
        print('運算公式輸入錯誤')
    choose = input('是否繼續?(Y or y=繼續；')
    if choose not in ('Y', 'y'):
        condition = False

condition = True
while (condition):
    computer()

# means 3
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def computer(figure1, figure2, operator):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    if operator in operations:
        result = operations[operator](figure1, figure2)
        print(f'計算結果 = {result}')
    else:
        print('運算公式輸入錯誤')


choose = 'Y'
while choose in ('Y', 'y'):
    num1 = int(input('請輸入第1個數字 = '))
    num2 = int(input('請輸入第2個數字 = '))
    ope = input('請輸入運算子(+, _, *, /)：')
    computer(num1, num2, ope)
    choose = input('是否繼續?(Y or y) = 繼續：')

print('程式結束')
