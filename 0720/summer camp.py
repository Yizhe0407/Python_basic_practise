# 2023/07/20
Math = {'Peter', 'Norton', 'Kevin', 'Mary', 'John',
        'Ford', 'Nelson', 'Damon', 'Ivan', 'Tom'}
Computer = {'Curry', 'James', 'Mary', 'Turisa',
            'Tracy', 'Judy', 'Lee', 'Jarmul', 'Damon', 'Ivan'}
Physics = {'Eric', 'Lee', 'Kevin', 'Mary', 'Christy',
           'Josh', 'Nelson', 'Kazil', 'Linda', 'Tom'}

print(f'同時參加3個夏令營名單：{Math & Computer & Physics}')
print(f'同時參加Math和Computer夏令營名單：{Math & Computer}')
print(f'同時參加Math和Physics夏令營名單：{Math & Physics}')
print(f'同時參加Computer和Physics夏令營名單：{Computer & Physics}')

