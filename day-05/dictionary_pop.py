#Dictionary থেকে নির্দিষ্ট Key-Value মুছতে pop() ব্যবহার করা যায়:
birds = {
    "name": "Pigeon",
    "color": "Gray",
    "age": 5
}

birds.pop("age")

print(birds)
#pop("age") → "age" Key এবং তার Value দুটোই মুছে দিয়েছে।
#আর পুরো Dictionary খালি করতে
#birds.clear()


birds = {
    "name": "Pigeon",
    "color": "Gray",
    "age": 5,
    "country": "Bangladesh"
}
birds.pop("age")
birds.pop("country")
print(birds)
print(birds.keys())#Dictionary-র সব Key দেখতে:
print(birds.values())#সব Value দেখতে:
print(birds.items())#Key এবং Value দুটো একসাথে দেখতে:
"""keys() → শুধু Key
values() → শুধু Value
items() → Key + Value"""

#chalange
student = {
    "name": "Abedin",
    "age": 28,
    "country": "Bangladesh"
}

print(student.keys())
print(student.values())
print(student.items())