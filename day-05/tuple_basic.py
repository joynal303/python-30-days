birds = ("Pigeon", "Parrot", "Dove", "Eagle")

print(birds[0])
print(birds[2])
print(len(birds))

#Tuple দেখতে List-এর মতো, কিন্তু এর Item পরিবর্তন করা যায় না। একে বলা হয় Immutable।
"""birds = ["Pigeon", "Parrot", "Dove"]
birds[0] = "Eagle"  # সম্ভব"""
"""birds = ("Pigeon", "Parrot", "Dove")
birds[0] = "Eagle"  # Error হবে"""

numbers = (10, 20, 30, 40, 50)

print(numbers[1])
print(numbers[-1])
print(len(numbers))
print(30 in numbers)

#১. count() — কোনো Value কতবার আছে তা গণনা করে।
numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))

#২. index() — কোনো Value প্রথম কোন Index-এ আছে তা জানায়।
birds = ("Pigeon", "Parrot", "Dove", "Parrot")

print(birds.index("Parrot"))
#Practice Challenge
birds = ("Pigeon", "Parrot", "Dove", "Eagle", "Parrot", "Crow")

print(birds.count("Parrot"))
print(birds.index("Crow"))
print(birds[2:5])



