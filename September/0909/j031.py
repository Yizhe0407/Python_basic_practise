while True:
    a, b, c, d, l = map(int, input().split())
    if a == b == c == d == l == 0:
        break
    if a >= -1000 and a <= 1000 and b >= -1000 and b <= 1000 and c >= -1000 and c <= 1000:
        if d > 1 and d < 1000000 and l >= 0 and l < 1000:
            divisible = 0
            for x in range(0, l + 1):
                f = a * (x ** 2) + (b * x) + c
                if f % d == 0:
                    divisible += 1
            print(divisible)
