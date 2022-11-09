class Droid:
    def __init__(self, name,model):
        self.name = name
        self.model = model



class Shop:
    def __init__(self):
        self.droids = [Droid("C3po"), Droid("R2D2"), Droid("BB8")]
        self.count = len(self.droids)

    def addDroid(self, newDroid):
            self.Droid.append(newDroid)

    def delDroid(self, delDroid):
        self.Droid.remove(delDroid)

    def __init__(self):
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

ShowInfo = Shop
ShowInfo = Droid