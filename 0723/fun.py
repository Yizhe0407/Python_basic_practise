# 2023/07/23
# f(i) = 1 + 1/2 + 1/3 + ... + 1/n
def fun(n):
    if n == 1:
        return 1
    else:
        return fun(n - 1) + 1.0 / n

n = eval(input('請輸入整數 : '))
for i in range(1, n + 1):
    print(f"{i}) = {fun(i):5.3f}") 


# f(i) = 1/2 + 1/3 + ... + n/(n+1)
def fun(n):
    if n == 1:
        return 1 / 2
    else:
        return fun(n - 1) + n / (n + 1)

n = eval(input('請輸入整數 : '))
for i in range(1, n + 1):
    print(f"{i}) = {fun(i):5.3f}") 