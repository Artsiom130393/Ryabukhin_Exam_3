#дописать классы Company, Programmer.

class Company:
    levels = {1: "junior", 2: "middle", 3: "senior", 4: "lead"}

    def __init__(self, index):
        if index > 4: index = 4
        self._index = index
        self._levels = self.levels[self._index]

    def _level_up(self):
        if self._index != 4:
            self._index += 1
            self._levels = self.levels[self._index]
            print('Уровень повышен до:', self._levels)

    def s_lead(self):
        if self._index == 4:
            print('Достигнут максимальный уровень!')
        else:
            print('Ваш уровень слишком мал! ', self.levels[self._index])
        return self._index == 4


class Programmer(Company):

    def __init__(self, name, uroven):
        super().__init__(uroven)
        self.name = name

    def work(self):
        self._level_up()

    @staticmethod
    def knowledge_base():
        print("Учение свет!", Company.levels)


pandadoc = Company(1)
artsiom = Programmer('Artsiom', 1)
artsiom.knowledge_base()
while artsiom.s_lead() == False:
    artsiom._level_up()
artsiom.s_lead()

