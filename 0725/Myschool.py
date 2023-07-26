# 2023/07/25
class Myschool():
    #schoolname = 'Python School'
    def __init__(self, name, score):
        self.name = name.title()
        self.score = score
        self.schoolname = 'Python School'

    def msg(self):
        print(self.schoolname)
        print('Hi!' + self.name + '你的成績是80分') 


hung = Myschool('kevin', 80)
hung.msg()

