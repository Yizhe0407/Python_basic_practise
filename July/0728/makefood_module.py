# 2023/07/28
def make_icecream(icecream_type, *toppings):
    """ 列出製作冰淇淋的配料 """
    print(f"這個 {icecream_type} 冰淇淋所加配料如下")
    for topping in toppings:
        print("--- ", topping)

def make_drink(size, drink):
    print("所點入飲料如下")
    print("--- ", size.title())
    print("--- ", drink.title())

def make_noodle(sort, *ingredients):
    print(f"{sort} 的配料如下：")
    for ingredient in ingredients:
        print("--- ", ingredient)

