cocktail = {
    'Blue Hawaiian': {'Rum', 'sweet wine', 'Wine', 'Gream', 'Pineapple Juice', 'Lemon Juice'},
    'Ginger Mojito': {'Rum', 'Ginger', 'Mint' 'Leaves', 'Lime Juice', 'Ginger Soda'},
    'New Yorker': {'Whiskey', 'Red Wine', 'Lemon Juice', 'Sugar Syrup'},
    'Bloody Mary': {'Vodka', 'Lemon Juice', 'Tomato Juice', 'Tabasco', 'little  Sale'},
    'Horse\'s Neck': {'brandy', 'ginger soda'},
    'Cosmopolitan': {'Vodka', 'sweet wine', 'lime Juice', 'cranberry juice'},
    'Sex on the Beach': {'Vodka', 'Peach Liqueur', 'orange juice', 'cranberry juice'}
}
print('含有Vodka的酒：')
for name, formulas in cocktail.items():
    if 'Vodka' in formulas:
        print(name)
print('含有sweet wine的酒：')
for name, formulas in cocktail.items():
    if 'sweet wine' in formulas:
        print(name)
print('含有Vodka和cranberry juice的酒：')
for name, formulas in cocktail.items():
    if 'Vodka' and 'cranberry juice' in formulas:
        print(name)
print('含有Vodka但是沒有cranberry juice的酒：')
for name, formulas in cocktail.items():
    if 'Vodka' in formulas and 'cranberry juice' not in formulas:
        print(name)