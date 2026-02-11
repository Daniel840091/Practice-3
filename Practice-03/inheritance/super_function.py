class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Person: {self.name}"

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def info(self):
        return f"{super().info()}, major={self.major}"

s = Student("Daniel", "IT")
print(s.info())
