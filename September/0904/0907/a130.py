
# ! 分批輸入
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
    for address in most_relevant:
        print(address)

# ! 一次性输入(執行速度較快)
amounts = int(input())

results = []

for amount in range(1, amounts + 1):
    highest = -1
    most_relevant = []

    for i in range(10):
        key, values = input().split()
        value = int(values)

        if value > highest:
            highest = value
            most_relevant = [key]
        elif value == highest:
            most_relevant.append(key)

    results.append((amount, most_relevant))

for amount, most_relevant in results:
    print(f'Case #{amount}:')
    for address in most_relevant:
        print(address)
