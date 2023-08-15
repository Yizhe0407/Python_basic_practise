try:
    while True:
        n, m = map(int, input().split())
        total = n
        num = 1
        while total <= m:
            total += n + num
            num += 1
        print(num)
except EOFError:
    pass
