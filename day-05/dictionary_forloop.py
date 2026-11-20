#Dictionary-এর Key এবং Value একসঙ্গে ব্যবহার করে Loop চালানো যায়।
student = {
    "name": "Abedin",
    "age": 28,
    "country": "Bangladesh"
}
for key, value in student.items():
    print(key, ":", value)

"""key প্রতিবার একটি Key গ্রহণ করছে।

value সেই Key-এর Value গ্রহণ করছে।

items() Key ও Value জোড়ায় দেয়।"""

birds = {
    "bird1": "Pigeon",
    "bird2": "Parrot",
    "bird3": "Dove",
    "bird4": "Eagle"
}

for key, value in birds.items():
    print(key, ":", value)

#get() Method
#Dictionary থেকে Value বের করতে আমরা এতক্ষণ ব্যবহার করেছি:
print(birds["bird1"])
#কিন্তু কোনো Key না থাকলে এটি KeyError দেবে।
print(birds.get("bird1"))
print(birds.get("bird5"))
#get()-এর আরেকটি সুবিধা হলো Default Value দেওয়া যায়:
print(birds.get("bird5", "Not Found"))


#Practice Challenge
birds = {
    "bird1": "Pigeon",
    "bird2": "Parrot",
    "bird3": "Dove"
}

print(birds.get("bird1"))
print(birds.get("bird4"))
print(birds.get("bird4", "Not Found"))

"""birds.get("bird1") → Key আছে, তাই Pigeon।
birds.get("bird4") → Key নেই, তাই None।
birds.get("bird4", "Not Found") → Key নেই, তাই Default Value Not Found।"""
