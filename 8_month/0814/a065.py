chart = dict(enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1))
flipped_chart = {value: key for key, value in chart.items()}
code = input()
password = [str(abs(flipped_chart[code[i]] - flipped_chart[code[i + 1]]))
            for i in range(6)]
print(''.join(password))
