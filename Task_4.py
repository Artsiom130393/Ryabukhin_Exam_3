# Создайте класс на тему животных.
# Используйте статические и динамические переменные,
# дочерний (1 или более) классов на конкретное животное.
# Публичные и приватные методы.
# Полиморфизм (одинаковые названия методов info в обоих классах,
# которые выводят информацию о животных,
# либо о конкретном животном данного класса).
# Создайте объекты каждого класса и обратитесь к каждому методу.
# Напишите один staticmethod,
# один classmethod, к которым также обратитесь.


class Animals:
    zoo = "Hello zoo!"
    pred = "хищные животные"
    herb = "травоядные животные"

    def __init__(self, predator):
        self.predator = predator
        self.predators = self.pred
        self.herbivores = self.herb

    def proveka(self):
        if self.predators == self.predator:
            print('Не подходите близко к клетке! Животное кусается!')
        elif self.herbivores != self.predator:
            print('Животное можно кормить!')

    def _food(self, meat, feed):
        self._meat = meat
        self._feed = feed
        if self._meat == self.pred:
            print(f'Животное - хищник! Ест {self._meat}')
        elif self._feed == self.herb:
            print(f'Животное - хищник! Ест {self._feed}')

    @classmethod
    def animals_zoo(cls):
        print(f'В нашем зоопарке есть {cls.pred}, и {cls.herb}')

    @staticmethod
    def hellozoo ():
        print(f'Мы рады видеть вас в нашем зоопарке! {Animals.zoo}')


    @classmethod
    def animals_zoo(cls):
        print(f'В нашем зоопарке есть {cls.pred}, и {cls.herb}')

class Wolves(Animals):

    def __init__(self, name, tip):
        super().__init__(tip)
        self.name = name

    def info_zoo(self):
        print('Данный класс животных - волки, являются хищниками! ')


class Giraffes(Animals):
    def __init__(self, name, tip):
        super().__init__(tip)
        self.name = name

    def info_zoo(self):
        print('Данный класс животных - жирафы, являются травоядными! ')


a = Animals('Волк')
a.hellozoo() #статический метод
a.animals_zoo() #метод класса
a.proveka()

wow = Wolves ("Волчёк", 1)
wow.info_zoo()
cif = Giraffes ("Боря",2)
cif.info_zoo()









