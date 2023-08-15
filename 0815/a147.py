while True:
    num = int(input())
    if num == 0:
        break
    print(' '.join(str(i) for i in range(num) if i % 7 != 0))
