"""এবার Python-এর তৃতীয় Data Structure শিখব: Set।

Set হলো এমন একটি Collection যেখানে:
1. Duplicate Value রাখা যায় না।
2. Set-এর নির্দিষ্ট Index নেই।
3. Set পরিবর্তন করা যায় (Mutable)।
4. Set তৈরি করতে {} ব্যবহার করা হয়।"""


birds = {"Pigeon", "Parrot", "Dove", "Pigeon"}

print(birds)

#Output-এ Pigeon একবারই থাকবে। তবে Set-এর Item-এর ক্রম নির্দিষ্ট নয়।
numbers = {10, 20, 30, 10, 20, 40}

print(numbers)
print(len(numbers))
print(20 in numbers)


#১. add() — নতুন Item যোগ করা
birds = {"Pigeon", "Parrot", "Dove"}

birds.add("Eagle")

print(birds)

#২. remove() — Item মুছে ফেলা
birds.remove("Parrot")

print(birds)


#chalange
animals = {"Cat", "Dog", "Cow"}

animals.add("Goat")# Goat যোগ করো

animals.remove("Dog")# Dog মুছে ফেলো

print(animals)# পুরো Set Print করো

#মনে রাখবে, Set-এর Item-এর ক্রম নির্দিষ্ট নয়। তাই Output-এর ক্রম ভিন্ন হতে পারে।
