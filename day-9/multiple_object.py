class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def print_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Color:", self.color)

    def eat(self):
        print(self.name, "is eating.")

pet1 = Pet("Pigeon", 2, "Red")
pet2 = Pet("Parrot", 3, "Green")
pet3 = Pet("Dove", 4, "Yellow")

pet1.print_info()
pet2.print_info()
pet3.print_info()


pet1.eat()
pet2.eat()
pet3.eat()