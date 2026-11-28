#Polymorphism কী?
"""Poly = অনেক
Morph = রূপ
Parent class থেকে একই sound() method inherit করে আনার পর, 
Child class-গুলো সেটাকে override করে নিজের মতো কাজ করাতে পারে।
অর্থাৎ, একই method/interface বিভিন্ন object-এর জন্য বিভিন্নভাবে কাজ করতে পারে।
আগে আমরা Method Overriding শিখেছিলাম। Polymorphism বুঝতে সেটাই সবচেয়ে সহজ উদাহরণ।"""

"""class Animal:
    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")

dog = Dog()
cat = Cat()
animal = Animal()

animal.sound()
dog.sound()
cat.sound()"""

"""এখানে Polymorphism কোথায়?
আমরা প্রত্যেক object-এর জন্য আলাদা method call লিখিনি:
dog.sound()
cat.sound()
দুটো ক্ষেত্রেই method-এর নাম একই:
Dog  → Woof!
Cat  → Meow!
এটাই Polymorphism।
Parent class থেকে একই sound() method inherit করে আনার পর,
Child class-গুলো সেটাকে override করে নিজের মতো কাজ করাতে পারে।"""

"""#practice
class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Woof!")


class Cat(Animal):
    def sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.sound()   # Woof!
cat.sound()   # Meow!"""

"""এখানে Dog এবং Cat দুটোই Animal থেকে এসেছে এবং দুটোই parent-এর sound() method override করেছে।"""
 

#practice
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")

class Bird(Animal):
    def sound(self):
        print("Bird says: Chirp!")



dog = Dog()
cat = Cat()
bird = Bird()

dog.sound()
cat.sound()
bird.sound()