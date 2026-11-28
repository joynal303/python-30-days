"""যে জিনিসের দরকার নেই, তার ভিতরের জটিল details লুকিয়ে রেখে শুধু প্রয়োজনীয় অংশ দেখানোই Abstraction।
বাস্তব উদাহরণ: তুমি ATM-এ টাকা তুললে।
তুমি শুধু:
Card → PIN → Amount → Withdraw
এগুলো জানো। কিন্তু ATM-এর ভিতরে ব্যাংকের server কীভাবে balance check করছে, transaction কীভাবে process হচ্ছে—এসব তোমাকে জানতে হয় না।
এটাই Abstraction।"""

#Python-এ Abstraction, Python-এ সাধারণত ABC এবং abstractmethod ব্যবহার করে Abstraction করা হয়।

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
#"Animal-এর sound method থাকতে হবে।"কিন্তু কী sound হবে সেটা Child class ঠিক করছে।
"""Animal  ↓
"sound() অবশ্যই থাকতে হবে"  ↓
Dog  → Woof!
Cat  → Meow!
Bird → Chirp!"""
#একটা গুরুত্বপূর্ণ নিয়ম
#যদি কোনো class ABC থেকে inherit করে এবং তার মধ্যে @abstractmethod থাকে, তাহলে সেই abstract method implement না করে সরাসরি object তৈরি করা যায় না।
#animal = Animal(), এটা করা যাবে না। কারণ Animal শুধু একটি blueprint/rule দিয়েছে; sound() কী করবে সেটা Child class-কে implement করতে হবে।

#Practice
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()