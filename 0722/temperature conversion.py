def CtoF(C):
    F = C * (9/5) + 32
    return f'{C:5d}{F:15.2f}'


def FtoC(F):
    C = (F-32) * 5 / 9
    return f'{F:5d}{C:15.2f}'


CtoF_results = [CtoF(i) for i in range(21, 31)]
FtoC_results = [FtoC(i) for i in range(70, 116, 5)]

print('攝氏溫度' + ' ' * 5 + '華氏溫度' + ' |' + '  華氏溫度' + ' ' * 5 + '攝氏溫度')
print('=' * 47)
for c_result, f_result in zip(CtoF_results, FtoC_results):
    print(f'{c_result}  |  {f_result}')
