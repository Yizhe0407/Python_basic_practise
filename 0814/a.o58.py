how_many_number = int(input())
figure = []
for i in range(how_many_number):
    figure.append(int(input()) % 3)
print(figure.count(0), figure.count(1), figure.count(2))
