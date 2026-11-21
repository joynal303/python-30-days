#age = int(input("Enter your age: "))#twenty
#ValueError দেবে, কারণ "twenty"-কে int বানানো যায় না

"""try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Please enter a valid number")"""

#challenge
"""try:
    age=int(input("Enter your age:"))
    print(f"Your age is {age}")
except ValueError:
    print("Please enter a valid number")"""

#Challenge 02, এবার ZeroDivisionError এবং ValueError দুটো একসাথে handle করবে।
try:
    a=int(input("Enter your first value:"))
    b=int(input("Enter your second value:"))

    print("Result:", a/b)
except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")