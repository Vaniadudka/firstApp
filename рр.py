class Student:
    count_students = 0
    def __init__(self, name, height):
        self.name = name
        self.height = height
        Student.count_students += 1
    def printer(self):
        print("Name:  ", self.name,    "Hight:  ", self.height)


    def set_name(self, newName):
        self.name = newName

first_student = Student("Vova    ", 150)
first_student.printer()
first_student.set_name("Vovan    ")
first_student.printer()
second_student = Student("Lesha   ", 140)
second_student.printer()
second_student.set_name("Lexich   ")
second_student.printer()

print(Student.count_students)