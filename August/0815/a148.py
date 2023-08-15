try:
    while True:
        subject = list(map(int, input().split()))
        sum = 0
        for i in range(len(subject) - 1):
            sum += subject[i + 1]
        print('no' if sum / subject[0] > 59 else 'yes')
except EOFError:
    pass
