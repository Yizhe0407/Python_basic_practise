amounts = int(input())

for amount in range(1, amounts + 1):
    information = {}
    for i in range(10):
        key, values = input().split()
        information[key] = int(values)
    highest = max(information.values())

    most_relevant = []
    for key, values in information.items():
        if values == highest:
            most_relevant.append(key)
    print(f'Case #{amount}:')
    for i in most_relevant:
        print(i)
