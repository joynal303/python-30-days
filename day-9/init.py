#1️⃣ __init__() কী?
""""__init__() হলো এমন একটি special method, যেটা object তৈরি হওয়ার সময় automatically run হয়।"""

"""class Student:
    def __init__(self):
        print("Student object created!")

student1 = Student()"""
"""student1 = Student() লেখার সাথে সাথে __init__() automatically call হবে।"""

#2️⃣ self কী?
#self বলতে বর্তমান object-কে বোঝায়।
"""class Student:
    def __init__(self):
        self.name = "Abedin"
        self.age = 28

student1 = Student()

print(student1.name)
print(student1.age)"""
#self.name = "Abedin", এই object-এর name হবে "Abedin"।
#self.age = 28, এই object-এর age হবে 28।

#3️⃣ কেন self দরকার?
#এবার দুইজন student তৈরি করি:
class Student:
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

student1 = Student("Abedin", 28, "CSE")
student2 = Student("Rahim", 25, "EEE")

print(student1.name)
print(student1.age)
print(student1.dept)

print(student2.name)
print(student2.age)
print(student2.dept)