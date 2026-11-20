#Pet Information Management System

"""আমরা এমন একটি ছোট Python প্রোগ্রাম তৈরি করব, যেখানে পোষা প্রাণীর তথ্য রাখা, দেখা এবং খাবারের তালিকা পরিবর্তন করা যাবে।"""
#1
"""pet = {
    "name": "Pigeon",
    "age": 2,
    "color": "White",
    "foods": ["Rice", "Corn", "Wheat"]
}

print(pet["name"])
print(pet["age"])

for i in pet["foods"]:
    print(i)

pet["foods"].append("Millet")
pet['age']=3
print(pet)"""
#2
"""food_name=input("Enter a food name:")
pet = {
    "name": "Pigeon",
    "age": 2,
    "color": "White",
    "foods": ["Rice", "Corn", "Wheat"]
}

print(pet["name"])
print(pet["age"])

for i in pet["foods"]:
    print(i)

pet["foods"].append("Millet")
pet["foods"].append(food_name)
pet['age']=3
print(pet)"""

#3
"""pet = {
    "name": "Pigeon",
    "age": 2,
    "color": "White",
    "foods": ["Rice", "Corn", "Wheat"]
}

choice = input("Enter 1 to add food or 2 to view foods: ")

if choice == "1":
    food_name = input("Enter a food name: ")
    pet["foods"].append(food_name)

    for i in pet["foods"]:
        print(i)

elif choice == "2":
    for i in pet["foods"]:
        print(i)

else:
    print("Invalid value")

print(pet)"""

#4

"""Python-এর ৪টি গুরুত্বপূর্ণ Data Structure



১. List — একাধিক Data সংরক্ষণ
Mutable — পরিবর্তন করা যায়
birds = ["Pigeon", "Parrot", "Dove", "Eagle"]



মূল বৈশিষ্ট্য:
- একাধিক Data রাখা যায়।
- Duplicate Value রাখা যায়।
- Index ব্যবহার করে Data Access করা যায়।
- Data যোগ, পরিবর্তন ও মুছে ফেলা যায়।
- [x] ব্যবহার করা হয়।
গুরুত্বপূর্ণ Methods:
Method	কাজ
append()	নতুন Item যোগ
insert()	নির্দিষ্ট জায়গায় যোগ
remove()	Item মুছে ফেলা
pop()	Index অনুযায়ী মুছে ফেলা
sort()	সাজানো
copy()	Copy তৈরি
clear()	সব মুছে ফেলা

কখন ব্যবহার করবে? যখন একাধিক Data রাখতে হবে এবং পরবর্তীতে সেগুলো পরিবর্তন করতে হবে।





২. Tuple — নির্দিষ্ট Data সংরক্ষণ
Immutable — পরিবর্তন করা যায় না
bird_info = ("Pigeon", 3, "White")



মূল বৈশিষ্ট্য:
- একাধিক Data রাখা যায়।
- Duplicate Value রাখা যায়।
- Index ব্যবহার করে Data Access করা যায়।
- তৈরি করার পর Item পরিবর্তন, যোগ বা মুছে ফেলা যায় না।
- () ব্যবহার করা হয়।
গুরুত্বপূর্ণ Methods:
Method	কাজ
count()	কোনো Value কতবার আছে
index()	Value-এর Index খুঁজে বের করা

কখন ব্যবহার করবে? যখন Data নির্দিষ্ট থাকবে এবং দুর্ঘটনাবশত পরিবর্তন হওয়া থেকে রক্ষা করতে চাও।




৩. Set — Unique Data সংরক্ষণ
Mutable — পরিবর্তন করা যায়
bird_types = {"Pigeon", "Parrot", "Dove", "Pigeon"}



Output:
{"Pigeon", "Parrot", "Dove"}



মূল বৈশিষ্ট্য:
- Duplicate Value রাখে না।
- নির্দিষ্ট Index নেই।
- Data যোগ ও মুছে ফেলা যায়।
- set() অথবা {} ব্যবহার করা হয়।
- Empty Set তৈরিতে set() ব্যবহার করতে হয়; {} হলো Empty Dictionary।
গুরুত্বপূর্ণ Methods:
Method	কাজ
add()	Item যোগ
remove()	Item মুছে ফেলা
discard()	Item মুছে ফেলা, না থাকলেও Error নেই
union()	দুই Set-এর সব Unique Item
intersection()	দুই Set-এর Common Item
difference()	প্রথম Set-এর আলাদা Item

কখন ব্যবহার করবে? যখন Duplicate Data বাদ দিতে হবে অথবা দুইটি Data Group-এর মধ্যে মিল-অমিল বের করতে হবে।





৪. Dictionary — Key-Value Data সংরক্ষণ
Mutable — পরিবর্তন করা যায়
pet = {    "name": "Pigeon",    "age": 3,    "color": "White"}



মূল বৈশিষ্ট্য:
- Key এবং Value জোড়ায় Data রাখে।
- প্রতিটি Key Unique হতে হয়।
- Key দিয়ে Value Access করা হয়।
- Data যোগ, পরিবর্তন ও মুছে ফেলা যায়।
- {} ব্যবহার করা হয়।
গুরুত্বপূর্ণ Methods:
Method	কাজ
get()	Key দিয়ে Value পাওয়া
keys()	সব Key পাওয়া
values()	সব Value পাওয়া
items()	Key-Value জোড়া পাওয়া
update()	Data যোগ বা পরিবর্তন
pop()	নির্দিষ্ট Key মুছে ফেলা
copy()	Copy তৈরি
clear()	সব Data মুছে ফেলা

কখন ব্যবহার করবে? যখন Data-কে নাম, বয়স, রং, ঠিকানা ইত্যাদি নির্দিষ্ট পরিচয়ের মাধ্যমে সংরক্ষণ করতে হবে।

চারটির মূল পার্থক্য এক নজরে
বৈশিষ্ট্য	List	Tuple	Set	Dictionary
Syntax	[]	()	{}	{key:value}
Mutable	হ্যাঁ	না	হ্যাঁ	হ্যাঁ
Duplicate	হ্যাঁ	হ্যাঁ	না	Key-তে না
Index	হ্যাঁ	হ্যাঁ	না	Key দিয়ে
Data Format	Value	Value	Unique Value	Key-Value

কোনটি সবচেয়ে বেশি প্রয়োজন?
তোমার লক্ষ্য যেহেতু Python থেকে AI Engineering শেখা, তাই আমার পরামর্শ:
১. List
অত্যন্ত গুরুত্বপূর্ণ

Machine Learning-এর Data, Dataset এবং বিভিন্ন Collection নিয়ে কাজ করতে List কাজে লাগে।

২. Dictionary
অত্যন্ত গুরুত্বপূর্ণ

JSON, API Response, Configuration এবং Structured Data নিয়ে কাজ করতে খুব প্রয়োজন।

৩. Tuple
গুরুত্বপূর্ণ

Fixed Data, Function থেকে একাধিক Value Return এবং কিছু Data Processing কাজে লাগে।

৪. Set
গুরুত্বপূর্ণ

Unique Data, Duplicate Removal এবং Set Operations-এর জন্য প্রয়োজন।

এটি শেখার অগ্রাধিকারের তালিকা, ব্যবহারের কোনো কঠোর Ranking নয়। চারটিই জানা দরকার।
AI Engineering-এ এগুলো কীভাবে কাজে লাগবে?
একটি ছোট উদাহরণ দেখো:
student = {    "name": "Abedin",    "skills": ["Python", "Django", "Machine Learning"],    "age": 28,    "completed_days": (1, 2, 3, 4, 5),    "unique_topics": {"Python", "AI", "Python"}}



এখানে:
- Dictionary দিয়ে Student-এর Profile রাখা হয়েছে।
- List দিয়ে Skills রাখা হয়েছে।
- Tuple দিয়ে নির্দিষ্ট Completed Days রাখা হয়েছে।
- Set দিয়ে Duplicate Topic বাদ দেওয়া হয়েছে।
এ ধরনের Data Structure বাস্তব Software ও AI Project-এ কাজে লাগবে।"""
