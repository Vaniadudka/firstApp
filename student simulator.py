import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 0

        self.alive = True

    def to_work(self):
        print("Time to work")
        self.progress += 0.7
        self.money += 100
        self.gladness -= 0.5

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.progress -= 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress < -0.5:
            print("Good buy Univer")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.money <= 0:
            print("No money good buy Univer")
            self.alive = False

    def endofDay(self):
        print("Gladness: ", self.gladness)
        print("Progress: ", self.progress)
        print("Money: ", self.money)

    def live(self, day):
        print("Day", str(day), " of ", self.name, "life")
        num = random.randint(1, 3)
        if num == 1:
            self.to_study()
        elif num == 2:
            self.to_chill()
        elif num == 3:
            self.to_sleep()

        self.endofDay()
        self.is_alive()

Lesha = Student("nick")
for day in range(365):
    if Lesha.alive == False:
        break
    Lesha.live(day)
