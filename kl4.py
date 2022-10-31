number = 100


class Number:
    # єто атрибут (переменная класс)
    num1 = 1
    num2 = 2

    def __init__(self, name):
        self.name = name

    # єто метод - геттер
    def Print(self):
        print(self.num1 + self.num2)

    # это метод сеттер
    def changeNum(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


# myNum = Number("my num 1")
# # myNum.changeNum(10, 20)
# # myNum.Print()


# базовый класс
class Animal:
    # __ можно запретить использование атрибута
    __sherst = ""

    def __init__(self, name, ves, paroda):
        self.name = name
        self.ves = ves
        self.paroda = paroda

    def golos(self):
        pass

    def ShowInfo(self):
        print("Name: ", self.name, "Paroda: ", self.paroda, "ves: ", self.ves)


#   дочерний класс Dog созданый на основе базового Animal
class Dog(Animal):
    def __init__(self, name, ves, paroda):
        super().__init__(name, ves, paroda)

    def golos(self):
        print("Gav gav")


#   дочерний класс Dog созданый на основе базового Animal
class Cat(Animal):
    def __init__(self, name, ves, paroda):
        super().__init__(name, ves, paroda)

    def golos(self):
        print("mau mau")


class CatDog(Dog, Cat):
    pass


myDog = Dog("Bobik", 20, "Staff")
myDog.ShowInfo()
myDog.golos()

myCat = Cat("Barsik", 5, "Bengal")
myCat.ShowInfo()
myCat.golos()

catDog = CatDog("bill", 40, "catdog")
catDog.ShowInfo()