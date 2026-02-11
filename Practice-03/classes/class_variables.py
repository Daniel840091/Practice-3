class Student:
    school = "KBTU"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable

s1 = Student("Daniel")
s2 = Student("Aruzhan")

print(Student.school)
print(s1.name)
print(s2.name)
