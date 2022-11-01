# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
# class Zoo:
#     def __init__(self, name):
#         self.name = name
#         self.paroda = []
#         self.sieve = 10
#
#     def to_eat(self):
#         self.sieve += 5
#
# class Gruppa:
#     def __init__(self, name):
#         self.name = name
#         self.animals = []
#
#     def addAnimal(self, newAnimal):
#         self.animals.append(newAnimal)
#
#     def delAnimal(self, delAnimal):
#         self.animals.remove(delAnimal)
#
#     def feeding(self):
#         print(self.sieve)
#
#     def printAnimals(self):
#         print("Name of the grupp: ", self.name)
#         for st in self.animals:
#             print(st.name)
#
#
# zibro = Animal("zibro")
# crocodile = Animal("crocodile")
# monkey = Animal("monkey")
# wolf = Animal("wolf")
# hipo = Animal("hipo")
# elefant = Animal("elefant")
# panda = Animal("panda")
# bear = Animal("bear")
#
# gruppa1 =Gruppa("herbivores")
# gruppa1.addAnimal(zibro)
# gruppa1.addAnimal(monkey)
# gruppa1.addAnimal(hipo)
# gruppa1.addAnimal(elefant)
# gruppa1.addAnimal(panda)
#
# gruppa2 =Gruppa("xichniki")
# gruppa2.addAnimal(crocodile)
# gruppa2.addAnimal(wolf)
#
# gruppa3 =Gruppa("omnivores")
# gruppa3.addAnimal(bear)
#
#
# gruppa1.printAnimales()
# gruppa2.printAnimales()
# gruppa3.printAnimales()
#
