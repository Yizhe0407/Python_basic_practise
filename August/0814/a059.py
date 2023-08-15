square = []
for i in range(32):
    square.append(i * i)
how_many_number = int(input())

for i in range(how_many_number):
    sum = 0
    a = int(input())
    b = int(input())
    for k in square:
        if a <= k and b >= k:
            sum += k
    print(f'Case {i + 1}: {sum}')
