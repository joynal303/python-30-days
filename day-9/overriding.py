#🟢 Method Overriding কী?
"""যখন Child Class, Parent Class-এর একই নামের method নিজের মতো করে আবার লিখে, তখন তাকে Method Overriding বলে।"""

"""class Animal:
    def eat(self):
        print("Animal is eating.")
#এখন Bird Child Class-এ আমরা আবার eat() লিখলাম:

class Bird(Animal):
    def eat(self):
        print("Bird is eating seeds.")

bird1 = Bird()
bird1.eat()"""

#Output হবে:Bird is eating seeds.
"""কারণ Bird-এর নিজের eat() method আছে। তাই Python প্রথমে Child Class-এ eat() খুঁজবে এবং সেটি পেলে Parent-এর eat() ব্যবহার করবে না।"""

#Parent-এর method বনাম Child-এর overridden method
"""Animal
└── eat()
    → Animal is eating.

        ↓ inheritance

Bird
└── eat()
    → Bird is eating seeds."""

#Bird-এর eat() আসলে Parent-এর eat()-কে override করেছে।
#super() দিয়ে Parent-এর method-ও চালানো যায়
"""class Bird(Animal):
    def eat(self):
        super().eat()
        print("Bird is eating seeds.")

bird1 = Bird()
bird1.eat()

#super().eat()
#Parent Class-এর eat() method চালাও।"""


#practice

class Animal:
   def sound(self):
    print("Animal makes a sound.")

class Bird(Animal):
    def sound(self):
        print("Bird says: Chirp Chirp!")

bird1= Bird()
bird1.sound()
#self বলতে bird1 object-কে বোঝাচ্ছে। Bird.sound(bird1), def sound(self): same
