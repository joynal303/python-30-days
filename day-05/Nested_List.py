students = [
    ["Abedin", 28],
    ["Rahim", 25],
    ["Karim", 27]
]

print(students[0])
print(students[0][0])
print(students[1][1])

print(students[1][0])
print(students[2][1])

birds = [
    ["Pigeon", 2],
    ["Parrot", 5],
    ["Dove", 3]
]

print(birds[0][0])#Pigeon Print করো।
print(birds[1][1])#Parrot-এর সংখ্যা 5 Print করো।
print(birds[2][0])#Dove Print করো।
birds[2][1] = 10#Dove-এর সংখ্যা 3 পরিবর্তন করে 10 করো।
print(birds[2])
birds.append(["Eagle", 4])
print(birds)#1. পুরো birds List Print করো।


#Challenge
animals = [
    ["Cat", 2],
    ["Dog", 4],
    ["Cow", 10]
]

print(animals[1][0])
print(animals[2][1])
print(animals[1][0])
animals[0][1] = 5
print(animals[0])
animals.append(["Goat", 3])
print(animals) 