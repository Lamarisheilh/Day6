class Student:
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades

    def calculate_gpa(self):
        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Grades: {self.grades}, GPA: {self.calculate_gpa()}"

n = int(input("Enter number of students: "))
students =[]

for i in range(n):
    name = input("Enter name: ")
    id = input("Enter ID: ")
    grades_str = input("Enter grades: ")
    
    grades = []
    for g in grades_str.split():
        grades.append(int(g))

    s = Student(name, id, grades)
    students.append(s)

with open("grades.txt", "w") as f:
    for s in students:
        f.write(str(s) + "\n")