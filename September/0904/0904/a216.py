def f(n):
    if n == 1:
        return 1
    else:
        return n + f(n - 1)


def g(n):
    if n == 1:
        return 1
    else:
        return f(n) + g(n - 1)


try:
    while True:
        a = int(input())
        print(f(a), g(a))
except EOFError:
    pass
