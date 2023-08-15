num = int(input())
for _ in range(num):
    values = list(map(int, input()))
    sum = 1
    for value in values:
        sum *= value
    print(sum)
