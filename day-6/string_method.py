"""upper()	সব বড় হাতের অক্ষর	HELLO PYTHON
lower()	সব ছোট হাতের অক্ষর	hello python
title()	প্রতিটি শব্দের প্রথম অক্ষর বড়	Hello Python
capitalize()	প্রথম অক্ষর বড়	Hello python"""

text = "hello python"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

#challenge
name = "joynal abedin"

print(name.upper())
print(name.title())
print(name.capitalize())
print(name.lower())

#১. strip() — অতিরিক্ত Space সরানো
name = "   Abedin   "
print(name.strip())

#২. replace() — একটি Text পরিবর্তন করা
text = "I love Java"
print(text.replace("Java", "Python"))

#৩. split() — String-কে List-এ ভাগ করা
text = "Pigeon,Parrot,Dove"
birds = text.split(",")

print(birds)

#challenge
name = "   joynal abedin   "
text = "I love Python programming"
birds = "Pigeon,Parrot,Dove"

print(name.strip())
print(text.replace("Python", "AI"))
print(birds.split(","))

"""strip() মূল String পরিবর্তন করে না; নতুন String Return করে।
replace() নতুন String Return করে।
split() একটি List Return করে।"""

#Lesson 06: find() এবং count()

#find() — কোনো শব্দ বা Character কোথায় আছে খুঁজে বের করে।
text = "I love Python"

print(text.find("Python"))
print(text.find("love"))

#count() — কোনো Character বা শব্দ কতবার আছে গণনা করে।
text = "I love Python and I love AI"

print(text.count("love"))
print(text.count("I"))

text = "Python is easy. Python is powerful."

print(text.find("easy"))
print(text.find("Python"))
print(text.count("Python"))
print(text.count("is"))