#১. len() — List-এ কয়টি item আছে?

birds = ["Pigeon", "Parrot", "Dove", "Eagle"]

print(len(birds))

#২. in — কোনো item List-এ আছে কি না?
birds = ["Pigeon", "Parrot", "Dove", "Eagle"]

print("Pigeon" in birds)
print("Crow" in birds)


my_birds = ["Pigeon", "Parrot", "Dove", "Eagle", "Crow"]
print(len(my_birds))
print("Pigeon" in my_birds)
print("Chicken" in my_birds)
my_birds.remove("Dove")
print(len(my_birds))
