"""class Animal:
    def eat(self):
        print("Animal is eating.")
    
    def sleep(self):
        print("Animal is sleeping.")

class Bird(Animal):
    def fly(self):
        print("Bird is flying.")

bird1 = Bird()

bird1.eat()
bird1.sleep()
bird1.fly()"""


"""এবার একটু গুরুত্বপূর্ণ জায়গায় আসি: Child Class-এ __init__() ব্যবহার করা
 এবং Parent Class-এর __init__() থেকে data নেওয়া।
"""
"""class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "is eating.")

class Bird(Animal):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def fly(self):
        print(self.name, "is flying.")

    #এখানে Bird-এর নিজের __init__() আছে। তাই Bird object তৈরি করার সময় name, age, color নেওয়া যাবে:
bird1 = Bird("Pigeon", 2, "White")

print(bird1.name)
print(bird1.age)
print(bird1.color)
#কিন্তু এখানে একটা সমস্যা আছে, Parent Animal-এর __init__()-এও:self.name = name,self.age = age, Child Bird-এর মধ্যেও আবার:, অর্থাৎ একই code দুইবার লিখছি।
#এটা এড়ানোর জন্য Python-এ super() ব্যবহার করা যায়।

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
#Parent Animal class-এর __init__() method-টি চালাও।
#তাই Parent-এর:, self.name = name, self.age = age, automatically কাজ করবে।
#তারপর Child নিজের extra property:, self.color = color"""

#Practice
class Animal:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    def eat(self):
        print(f"The {self.name} is eating")
            
class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color= color

    def fly(self):
        print(f"The {self.name} is flying")

bird1 = Bird("Pigeon", 2, "White")