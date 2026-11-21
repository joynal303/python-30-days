#finally block সব পরিস্থিতিতেই execute হয়—Error হোক বা না হোক।

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

finally:
    print("Calculator session ended.")