"""Lesson 03: return Statement
এবার খুব গুরুত্বপূর্ণ একটি বিষয় শিখব।

print() শুধু ফলাফল দেখায়। কিন্তু return Function থেকে ফলাফল ফেরত দেয়, যাতে সেটি অন্য Variable বা Calculation-এ ব্যবহার করা যায়।"""

def add_number(a, b):
    return a + b

result = add_number(10, 20)

print(result)