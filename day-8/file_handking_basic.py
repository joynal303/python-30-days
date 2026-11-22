#Day 08 — File Handling (Python-এ ফাইল তৈরি, পড়া, লেখা ও সংরক্ষণ)
"""খানে আমরা শিখব:
- open()
- read()
- write()
- append()
- with open()
- close()"""

"""Lesson 01: File Handling কী?
ধরো, তুমি একটি Pet Information Management System তৈরি করেছ। সেখানে একটি Pigeon-এর তথ্য আছে:
pet_name = "Pigeon"
pet_age = 2
pet_color = "White"
এখন Python প্রোগ্রাম বন্ধ করলে এই Variable-এর তথ্য আর থাকবে না।

কিন্তু তুমি যদি তথ্যগুলো একটি .txt ফাইলে সংরক্ষণ করো, তাহলে প্রোগ্রাম বন্ধ করলেও তথ্য থাকবে।

এটাই File Handling-এর একটি গুরুত্বপূর্ণ ব্যবহার।"""


#Python-এ ফাইল খোলার জন্য open() ব্যবহার করা হয়।
#file = open("filename.txt", "mode")

"""Mode	কাজ
"r"	ফাইল পড়া (Read)
"w"	ফাইলে লেখা (Write)
"a"	আগের লেখার শেষে নতুন লেখা (Append)
"x"	নতুন ফাইল তৈরি"""

file = open("my_pet.txt", "w")

file.write("My pet name is Pigeon")
file.write("\nMy pet age is 2")

file.close()