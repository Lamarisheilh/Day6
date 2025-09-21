class Student:
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades

    def calculate_gpa(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Grades: {self.grades}, GPA: {self.calculate_gpa()}"


s1 = Student("Lamar", 39839, [90, 80, 60, 70])
print(f"{s1.name}'s GPA is {s1.calculate_gpa()}")