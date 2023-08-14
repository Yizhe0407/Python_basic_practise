city = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14',
        'F': '15', 'G': '16', 'H': '17', 'I': '34', 'J': '18',
        'K': '19', 'L': '20', 'M': '21', 'N': '22', 'O': '35',
        'P': '23', 'Q': '24', 'R': '25', 'S': '26', 'T': '27',
        'U': '28', 'V': '29', 'W': '32', 'X': '30', 'Y': '31',
        'Z': '33'}
last_9_yards = input()


def calculate(num):
    city = int(num[0])
    for i in range(1, 10):
        city += int(num[i]) * (10 - i)
    checksum = (10 - city % 10) if (10 - city % 10) != 10 else 0
    return (checksum == int(num[-1]))


for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if (calculate(city[i] + last_9_yards)):
        print(i, end='')
print()
