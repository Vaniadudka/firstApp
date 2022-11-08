number = 100
myList = [number, 2,3]


for i in myList:
    print(i)


myIterator = iter(myList)

# print(myIterator)
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))

for elem in myIterator:
    print(elem)







class Counter:
    def __init__(self, max_number):
        self.max_number = max_number
        self.i = 0

    def __int__(self):
        self.i = 0
        return self

    def __index__(self):
        self.i += 1
        return self.i


count = Counter(5)
print("==============================")
for elem in count:
    print(elem)

for elem in count:
    print(elem)