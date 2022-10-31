class Figure:
    Kolor = ""
    Pi = 3,14
    X = ""
    Y = ""

class Rectangle(Figure):
    def __init__(self):
        self.kolor = "black"
        self.X = 5
        self.Y = -1

    def changeNum(self, X, Y):
        self.X = 6
        self.Y = -3

    def Print(self):
        print(self.X)
        print(self.Y)