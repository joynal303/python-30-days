"""এটা File Handling-এর খুব গুরুত্বপূর্ণ অংশ, কারণ Python-এর dict এবং list data সুন্দরভাবে file-এ সংরক্ষণ করা যায়।"""
#Lesson 09: JSON কী?
"""JSON-এর পূর্ণরূপ JavaScript Object Notation।
সহজভাবে বললে, JSON হলো এমন একটি data format, যা মানুষ সহজে পড়তে পারে এবং বিভিন্ন programming language সহজে ব্যবহার করতে পারে।"""
"""#Python-এর এই Dictionary:
student = {
    "name": "Abedin",
    "age": 28,
    "country": "Bangladesh",
    "skill": "Python"
}
#JSON-এ প্রায় একইভাবে থাকবে:
{
    "name": "Abedin",
    "age": 28,
    "country": "Bangladesh",
    "skill": "Python"
}"""

#প্রথমে json module import করব:
#তারপর একটি Dictionary:
"""import json

student = {
    "name": "Abedin",
    "age": 28,
    "country": "Bangladesh",
    "skill": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file)"""

#এখানে json.dump() কী করে?
#এটি Python Dictionary-কে JSON format-এ convert করে student.json file-এ লিখে দেয়।

#Challenge 09
import json
pet={
    "name": "Pigeon",
    "age": 2,
    "color": "White",
    "food": "Rice"
}
with open("pet.json", "w") as file:
    json.dump(pet, file)

#এবার JSON থেকে Data আবার Python-এ আনব
#json.load()

"""import json
with open("pet.json", "r") as file:
    pet = json.load(file)
print(pet)"""

"""json.dump() → Python → JSON file
json.load() → JSON file → Python"""

#Challenge 10
"""with open("pet.json", "r") as my_file:
    pet=json.load(my_file)
    print(pet["name"])
    print(pet["age"])
    print(pet["color"])
    print(pet["food"])
    print(pet)
"""
import json

pet = {
    "name": "Pigeon",
    "age": 2,
    "color": "White",
    "food": "Rice"
}

with open("pet.json", "w") as my_file:
    json.dump(pet, my_file, indent=4)