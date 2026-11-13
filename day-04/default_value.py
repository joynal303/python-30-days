#এখানে name অবশ্যই দিতে হবে।

def greet(name):
    print("Hello", name)

greet("Abedin")


"""argument না দিলে → default value ব্যবহার হবে।
argument দিলে → দেওয়া value ব্যবহার হবে।"""

def greet(name="Abedin"):
    print("Hello", name)

greet()
greet("Rahim")