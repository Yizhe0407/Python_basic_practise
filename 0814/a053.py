right = int(input())
score = 0
if right == 40:
    print(100)
else:
    if right < 11:
        score = right * 6
    elif right > 10 and right < 21:
        score = 60
        score += (right - 10) * 2
    elif right > 20 and right < 41:
        score = 80
        score += right - 20
    elif right > 40:
        score = 100
    print(score)
