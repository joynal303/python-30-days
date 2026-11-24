#Inheritance কী?
"""একটি Class অন্য একটি Class-এর properties ও methods গ্রহণ করতে পারলে তাকে Inheritance বলে।"""
"""Animal → Parent Class
Pet → Child Class"""

class Animal:
    def eat(self):
        print("Animal is eating.")

    def sleep(self):
        print("Animal is sleeping.")

class Pet(Animal):
    def play(self):
        print("Pet is playing.")

"""এখানে Pet হলো Child Class এবং Animal হলো Parent Class।
অর্থাৎ Pet class এখন Animal-এর methods ব্যবহার করতে পারবে"""

pet1 = Pet()

pet1.eat()
pet1.sleep()
pet1.play()

"""Pet class-এর মধ্যে eat() এবং sleep() method লেখা হয়নি, তারপরও ব্যবহার করতে পারছে!
কারণ এগুলো Parent Class থেকে Inherit হয়েছে।"""
