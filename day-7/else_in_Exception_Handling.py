#Lesson: else in Exception Handling
#else block তখনই execute হবে, যখন try block-এ কোনো error হবে না।

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)