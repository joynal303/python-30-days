#এখন পর্যন্ত তুমি এভাবে pet-এর তথ্য রেখেছ:
"""pet = {
    "name": "Pigeon",
    "age": 2,
    "color": "White"
}
খানে সমস্যা হলো, অনেক pet হলে বারবার dictionary বানাতে হবে।
OOP-তে আমরা একটি Class বানিয়ে সেই structure বারবার ব্যবহার করতে পারি।"""

"""#1️⃣ Class কী?
Class = Object বানানোর blueprint / design
যেমন আমরা Pet নামের একটা design বানাব:
class Pet:
    pass
এখনো Pet-এর কোনো তথ্য বা কাজ নেই।"""

"""2️⃣ Object কী?
Class থেকে যখন কোনো বাস্তব instance তৈরি করি, সেটি Object।

class Pet:
    pass
pet1 = Pet()
pet2 = Pet()
print(pet1)
print(pet2)

Pet     → Class
pet1    → Object
pet2    → Object
অর্থাৎ একই Pet class থেকে একাধিক object তৈরি করা যায়।"""

"""3️⃣ Attribute কী?
Object-এর নিজের information-কে Attribute বলা হয়।
class Pet:
    pass

pet1 = Pet()
pet1.name = "Pigeon"
pet1.age = 2
pet1.color = "White"
print(pet1.name)
print(pet1.age)
print(pet1.color)

Pigeon
2
White

pet1.name
pet1.age
pet1.color
হলো pet1 object-এর attributes।"""

#Practice
class Student:
    name = "Abedin"
    age = 28
    department = "CSE"

student1 = Student()

print(student1.name)
print(student1.age)
print(student1.department)