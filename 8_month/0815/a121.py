def is_prime(range1, range2):
    primes = []
    for j in range(range1, range2 + 1):
        check = 1
        if j == 2:
            primes.append(j)
            continue
        if j % 2 == 0:
            check = 0
        for k in range(3, int(j**0.5) + 1, 2):
            if j % k == 0:
                check = 0
        if check == 1:
            primes.append(j)
    return len(primes)


try:
    while True:
        range1, range2 = map(int, input().split())
        if range2 - range1 <= 1000:
            print(is_prime(range1, range2))
except EOFError:
    pass
