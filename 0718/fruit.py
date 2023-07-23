# 2023/07/18
# method 1
fruits = {'Watermelon': 15, 'Banana': 20, 'Pineapple': 25, 'Orange': 12, 'Apple': 18}
print(fruits)
fruits2 = sorted(fruits.items())
for i in range(len(fruits2)):
    print(f"{fruits2[i][0]} : {fruits2[i][1]}" )

# method 2
fruits = {'Watermelon': 15, 'Banana': 20, 'Pineapple': 25, 'Orange': 12, 'Apple': 18}
print(fruits)
fruits2 = sorted(fruits.items())
for fruit, value in fruits2:
    print(f"{fruit} : {value}")
