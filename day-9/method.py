#🟢 Method কী?
#Class-এর ভিতরে কোনো function লিখলে সেটাকে সাধারণভাবে Method বলা হয়।
class Student:
    def introduce(self):
        print("Hello, I am a student.")
#এখানে introduce() হলো একটি method।
student1 = Student()
student1.introduce()
#Object দিয়ে method call করা যায়:

#আমরা চাই Student-এর নিজের পরিচয় নিজেই দেখাবে:
class Student:
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.dept)

student1 = Student("Abedin", 28, "CSE")
student2 = Student("Rahim", 25, "EEE")

student1.introduce()
student2.introduce()
#এখানে একই introduce() method দুইটা object-এর জন্য কাজ করছে।
