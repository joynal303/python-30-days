#Day 07 — Python Exception Handling
"""বাস্তব Software বা AI Project-এ Code সবসময় সঠিক Input পায় না।
 তখন Program যেন হঠাৎ বন্ধ না হয়ে যায়, সেজন্য Exception Handling প্রয়োজন।"""
"""a = 10
b = 0
print(a / b)"""
#কারণ কোনো সংখ্যাকে শূন্য দিয়ে ভাগ করা যায় না।
#এই ধরনের Error সামলাতে try-except ব্যবহার করা হয়।
"""try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")"""

"""try → যে Code-এ Error হতে পারে।
except → Error হলে কী করতে হবে।"""

#Challenge
try:
    a=int(input("Enter first Number:"))
    b=int(input("Enter second Number:"))

    print(a/b)

except ZeroDivisionError:
    print("Cannot divide by zero")