class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        
    def print_function(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Color:", self.color)

    def eat(self):
        print(self.name, "is eating.")

pet1 = Pet("Pigeon", 2, "Red")

pet1.print_function()
pet1.eat()