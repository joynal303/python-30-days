"""try:
    a=int(input("Enter your first number:"))
    b=int(input("Enter your second number:"))
    add= a+b
    sub= a-b
    mul= a*b
    div= a/b
except ZeroDivisionError:
    print(" Cant div by zero!")

except ValueError:
    print(" Iv valied value give corret value!")

else:
    print(f"Addition is: {add}\n Subtraction is: {sub}\n Multiplication is: {mul}\n Divition is: {div}")

finally:
    print("Finaly Excute the program")"""


try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))

    add = a + b
    sub = a - b
    mul = a * b
    div = a / b

except ZeroDivisionError:
    print("Can't divide by zero!")

except ValueError:
    print("Invalid input! Please enter a valid number.")

else:
    print(f"""
Addition: {add}
Subtraction: {sub}
Multiplication: {mul}
Division: {div}
""")

finally:
    print("Finally executed. Program ended!")