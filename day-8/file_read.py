file= open("student.txt")#or "r" Python-এ open()-এর Default Mode হলো "r" (Read Mode)।
data= file.read()
print(data)
file.close()

#এবার নতুন Lesson: readline()
"""read() সম্পূর্ণ ফাইল পড়ে।
অন্যদিকে readline() একবারে একটি লাইন পড়ে।"""
file = open("student.txt", "r")

data = file.readline()
print(data)

file.close()

#Challenge 03
file= open("student.txt", "r")
data= file.readline()
print(data)

data= file.readline()
print(data)

data= file.readline()
print(data)

data= file.readline()
print(data)

file.close()

#readlines() ফাইলের সব লাইন একসঙ্গে পড়ে একটি List হিসেবে Return করে।
file = open("student.txt", "r")

data = file.readlines()
print(data)

file.close()

#Challenge 04
file = open("student.txt", "r")

data = file.readlines()
for i in data:
    print(i,  end="")

file.close() 