class Student: 
     
     def __init__(self,name,id,grades): 
         self.name = name 
         self.id = id 
         self.grades = grades

     def calculate_gpa(self,scale=4.0): 
         r = sum(self.grades)/len(self.grades)
         return round((r/100)*scale , 2)

s1 = Student("Lamar", 39839, [90, 80, 70])
print(f"{s1.name}'s GPA is : {s1.calculate_gpa()}")