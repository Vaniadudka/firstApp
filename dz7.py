myList = []
Droid = "C3o", "R2D2", "BB8", "Bfd4", "Vds5", "BHKm9"
print(Droid)

for i in myList:
    print(i)


myIterator = iter(myList)

class Droid:
    def __init__(self, name,model):
        self.name = name
        self.model = model



class Shop:
    def __init__(self):
        self.droids = [Droid("C3po"), Droid("R2D2"), Droid("BB8"), Droid("Bfd4"), Droid("Vds5"), Droid("BHKm9")]
        self.count = len(self.droids)
        self.d = 0

    def __iter__(self):
        self.d = Droid
        return self

    def __next__(self):
        self.d += Droid
        return self.d

    def addDroid(self, newDroid):
            self.d.append(newDroid)

    def delDroid(self, delDroid):
        self.d.remove(delDroid)



ShowInfo = Shop

