# 2023/07/26
class Animals():
    """Animals類別, 這是基底類別 """
    def __init__(self, animal_name, animal_age ):
        self.name = animal_name # 紀錄動物名稱
        self.age = animal_age   # 紀錄動物年齡

    def run(self):              # 輸出動物 is running
        print(self.name.title(), " is running")

    def fly(self):
        print(self.name.title(), " is flying")


class Dogs(Animals):
    """Dogs類別, 這是Animal的衍生類別 """
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet ' + dog_name.title(), dog_age)

class Birds(Animals):
    def __init__(self, Bird_name, Bird_age):
        super().__init__('My pet ' + Bird_name, Bird_age)

mycat = Animals('lucy', 5)      
print(mycat.name.title(), ' is ', mycat.age, " years old.")
mycat.run()

mydog = Dogs('lily', 6)         
print(mydog.name.title(), ' is ', mydog.age, " years old.")
mydog.run()

mybird = Birds('Cici', 8)
print(mybird.name.title(), ' is ', mybird.age, " years old.")
mybird.fly()